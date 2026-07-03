from django.urls import path
from . import views


urlpatterns = [

    path('', views.home, name='home'),

    path('dashboard/', views.dashboard, name='dashboard'),


    # MATERIAIS

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


    # IMPRESSORAS

    path(
        'impressoras/',
        views.impressoras,
        name='impressoras'
    ),

    path(
        'impressoras/novo/',
        views.novo_impressora,
        name='novo_impressora'
    ),

    path(
        'impressoras/editar/<int:id>/',
        views.editar_impressora,
        name='editar_impressora'
    ),

    path(
        'impressoras/excluir/<int:id>/',
        views.excluir_impressora,
        name='excluir_impressora'
    ),



    # ORÇAMENTOS

    path(
        'orcamentos/',
        views.orcamentos,
        name='orcamentos'
    ),

    path(
         'orcamentos/novo/',
         views.novo_orcamento,
        name='novo_orcamento'
    ),

    path(
        'orcamentos/editar/<int:id>/',
        views.editar_orcamento,
        name='editar_orcamento'
    ),

    path(
        'orcamentos/excluir/<int:id>/',
        views.excluir_orcamento,
        name='excluir_orcamento'
    ),

]

