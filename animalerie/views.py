from django.shortcuts import render
from .models import Animal


def home(request):
    animaux = Animal.objects.all()

    return render(request, 'animalerie/home.html', {'animaux': animaux})
