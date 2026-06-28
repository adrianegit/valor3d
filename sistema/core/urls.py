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

    path('impressoras/', views.impressoras, name='impressoras'),

    path('orcamentos/', views.orcamentos, name='orcamentos'),

]