from django.shortcuts import render
from .models import Material, Impressora, Orcamento


def home(request):

    return render(request, 'core/home.html')



def dashboard(request):

    contexto = {

        'total_materiais': Material.objects.count(),

        'total_impressoras': Impressora.objects.count(),

        'total_orcamentos': Orcamento.objects.count(),

    }


    return render(request, 'core/dashboard.html', contexto)