from django.urls import path
from django.contrib.auth import views as auth_views
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

path(
    'orcamentos/<int:id>/',
    views.detalhe_orcamento,
    name='detalhe_orcamento'
),

    path(
        "configuracao/",
        views.configuracao_custo,
        name="configuracao_custo",
    ),

]

# RECUPERAÇÃO DE SENHA DE LOGIN

path(
    'password_reset/',
    auth_views.PasswordResetView.as_view(
        template_name='registration/password_reset_form.html'
    ),
    name='password_reset'
),

path(
    'password_reset/done/',
    auth_views.PasswordResetDoneView.as_view(
        template_name='registration/password_reset_done.html'
    ),
    name='password_reset_done'
),

path(
    'reset/<uidb64>/<token>/',
    auth_views.PasswordResetConfirmView.as_view(
        template_name='registration/password_reset_confirm.html'
    ),
    name='password_reset_confirm'
),

path(
    'reset/done/',
    auth_views.PasswordResetCompleteView.as_view(
        template_name='registration/password_reset_complete.html'
    ),
    name='password_reset_complete'
),