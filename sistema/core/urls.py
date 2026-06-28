from django.urls import path
from . import views


urlpatterns = [

    path('', views.home, name='home'),

    path('dashboard/', views.dashboard, name='dashboard'),

    path('materiais/', views.materiais, name='materiais'),

    path(
        'materiais/novo/',
        views.novo_material,
        name='novo_material'
    ),

    path(
        'materiais/editar/<int:id>/',
        views.editar_material,
        name='editar_material'
    ),

    path(
        'materiais/excluir/<int:id>/',
        views.excluir_material,
        name='excluir_material'
    ),

]