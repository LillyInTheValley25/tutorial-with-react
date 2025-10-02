from django.urls import path
from . import views

urlpatterns = [
    path('dinosaurs/', views.get_all_dinosaurs, name='get_all_dinosaurs'),
    path('dinosaurs/<str:dinosaur_name>/', views.get_dinosaur_by_name, name='get_dinosaur_by_name'),
]
