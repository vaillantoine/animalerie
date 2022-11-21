from django.shortcuts import render, get_object_or_404, redirect
from .models import Animal
from .forms import MoveForm


def animal_list(request):
    animaux = Animal.objects.all()

    return render(request, 'animalerie/animal_list.html', {'animaux': animaux})


def animal_detail(request, id_animal):
    animal = get_object_or_404(Animal, id_animal=id_animal)
    lieu = animal.lieu
    form = MoveForm()
    return render(request,
                  'animalerie/animal_detail.html',
                  {'animal': animal, 'lieu': lieu, 'form': form})
