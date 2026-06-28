from django.shortcuts import render, redirect, get_object_or_404
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

    material = get_object_or_404(Material, id=id)

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


def editar_material(request, id):

    material = get_object_or_404(Material, id=id)


    if request.method == 'POST':

        form = MaterialForm(
            request.POST,
            instance=material
        )


        if form.is_valid():

            form.save()

            return redirect('/materiais/')


    else:

        form = MaterialForm(
            instance=material
        )


    return render(
        request,
        'core/material_form.html',
        {
            'form': form
        }
    )


def excluir_material(request, id):

    material = get_object_or_404(Material, id=id)

    material.delete()

    return redirect('/materiais/')