from django.urls import path, include
from . import views

urlpatterns = [
    path('_<str:pk>',views.compte,name='compte'),
    path('',views.compte,name='compte'),
    path('ajouprojet/',views.create_projet,name='create_projet'),
    path('ajo/',views.lister_projets,name='lister_projets'),
    path('open/',views.ouvrir_projet,name='client'),
    path('project_interface/',views.project_interface, name='project_interface'),
    path('p/',views.fr, name='fr'),
    path('project_list/',views.project_list, name='project_list'),
]
