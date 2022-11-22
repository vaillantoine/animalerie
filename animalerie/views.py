from django.shortcuts import render, get_object_or_404, redirect
from .models import Animal, Equipement
from .forms import MoveForm
from django.contrib import messages


def animal_list(request):
    animaux = Animal.objects.all()

    return render(request, 'animalerie/animal_list.html', {'animaux': animaux})


def animal_detail(request, id_animal):
    message = ''
    animal = get_object_or_404(Animal, id_animal=id_animal)
    ancien_etat = animal.etat
    ancien_lieu = get_object_or_404(Equipement, id_equip=animal.lieu.id_equip)
    form = MoveForm(request.POST, instance=animal)

    if form.is_valid():
        form.save(commit=False)
        nouveau_lieu = get_object_or_404(Equipement, id_equip=animal.lieu.id_equip)
        lieux_etats = {'litière': 'affamé',
                       'mangeoire': 'repus',
                       'roue': 'fatigué',
                       'nid': 'endormi'}
        nouveau_lieux_ancien_etat = {'mangeoire': 'affamé',
                                     'roue': 'repus',
                                     'nid': 'fatigué',
                                     'litière': 'endormi'}
        if (ancien_etat == nouveau_lieux_ancien_etat[nouveau_lieu.id_equip]) and (
                nouveau_lieu.disponibilite or (nouveau_lieu.id_equip == 'litière')):
            ancien_lieu.disponibilite = True
            ancien_lieu.save()
            nouveau_lieu.disponibilite = False
            nouveau_lieu.save()
            animal.etat = lieux_etats[nouveau_lieu.id_equip]
            animal.save()
            messages.success(request, f"{animal.id_animal} a été déplacé")
            return redirect('animal_detail', id_animal=id_animal)
        else:
            messages.error(request, "Action impossible")
    form = MoveForm()
    lieu = get_object_or_404(Equipement, id_equip=animal.lieu.id_equip)

    return render(request,
                  'animalerie/animal_detail.html',
                  {'animal': animal,
                   'lieu': lieu,
                   'form': form,})
