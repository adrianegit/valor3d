from django.shortcuts import render, redirect
from .models import Material, Impressora, Orcamento
from .forms import MaterialForm



def home(request):

    return render(request, 'core/home.html')



def dashboard(request):

    contexto = {

        'total_materiais': Material.objects.count(),

        'total_impressoras': Impressora.objects.count(),

        'total_orcamentos': Orcamento.objects.count(),

    }


    return render(request, 'core/dashboard.html', contexto)



def materiais(request):

    materiais = Material.objects.all()

    return render(
        request,
        'core/materiais.html',
        {
            'materiais': materiais
        }
    )



def impressoras(request):

    return render(request, 'core/impressoras.html')



def orcamentos(request):

    return render(request, 'core/orcamentos.html')


def novo_material(request):

    if request.method == 'POST':

        form = MaterialForm(request.POST)

        if form.is_valid():

            form.save()

            return redirect('/materiais/')


    else:

        form = MaterialForm()


    return render(
        request,
        'core/material_form.html',
        {
            'form': form
        }
    )