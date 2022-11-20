from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('animal/<str:id animal>/', views.animal_detail, name='animal_detail'),
    path('animal/<str:id_animal>/?<str:message>', views.animal_detail, name='animal_detail_mes'),
]
