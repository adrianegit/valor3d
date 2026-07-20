from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Material, Impressora, Orcamento, ConfiguracaoCusto 
from .forms import (
    MaterialForm,
    ImpressoraForm,
    OrcamentoForm,
    ConfiguracaoCustoForm,
)



def home(request):

    return render(request, 'core/home.html')


@login_required
def dashboard(request):

    contexto = {

        'total_materiais': Material.objects.count(),

        'total_impressoras': Impressora.objects.count(),

        'total_orcamentos': Orcamento.objects.count(),

    }


    return render(request, 'core/dashboard.html', contexto)



@login_required
def materiais(request):
    materiais = Material.objects.all()
    return render(
        request,
        "core/materiais.html",
        {
            "materiais": materiais
        }
    )


@login_required
def impressoras(request):

    impressoras = Impressora.objects.all()

    print("IMPRESSORAS:", impressoras)

    return render(
        request,
        'core/impressoras.html',
        {
            'impressoras': impressoras
        }
    )

@login_required
def novo_material(request):

    if request.method == 'POST':

        form = MaterialForm(request.POST)

        if form.is_valid():

            form.save()

            messages.success(
                request,
                "Material cadastrado com sucesso!"
            )

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



@login_required
def editar_material(request, id):

    material = get_object_or_404(Material, id=id)


    if request.method == 'POST':

        form = MaterialForm(
            request.POST,
            instance=material
        )


        if form.is_valid():

            form.save()

            messages.success(
                request,
                "Material atualizado com sucesso!"
            )

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

@login_required
def excluir_material(request, id):

    material = get_object_or_404(Material, id=id)

    material.delete()

    messages.success(
    request,
    "Material excluído com sucesso!"
    )

    return redirect('/materiais/')

@login_required
def novo_impressora(request):

    if request.method == "POST":

        form = ImpressoraForm(request.POST)

        if form.is_valid():

            form.save()

            messages.success(
                request,
                "Impressora cadastrada com sucesso!"
            )

            return redirect("/impressoras/")

    else:

        form = ImpressoraForm()

    return render(
        request,
        "core/impressora_form.html",
        {
            "form": form
        }
    )

@login_required
def editar_impressora(request, id):

    impressora = get_object_or_404(
        Impressora,
        id=id
    )

    if request.method == "POST":

        form = ImpressoraForm(
            request.POST,
            instance=impressora
        )

        if form.is_valid():

            form.save()

            messages.success(
                request,
                "Impressora atualizada com sucesso!"
            )

            return redirect("/impressoras/")

    else:

        form = ImpressoraForm(
            instance=impressora
        )

    return render(
        request,
        "core/impressora_form.html",
        {
            "form": form
        }
    )

@login_required
def excluir_impressora(request, id):

    impressora = get_object_or_404(
        Impressora,
        id=id
    )

    impressora.delete()

    messages.success(
    request,
    "Impressora excluída com sucesso!"
)

    return redirect("/impressoras/")

@login_required
def novo_orcamento(request):

    if request.method == "POST":

        form = OrcamentoForm(request.POST)

        if form.is_valid():

            orcamento = form.save()

            messages.success(
                request,
                "Orçamento cadastrado com sucesso!"
            )

            return redirect(
                "detalhe_orcamento",
                id=orcamento.id
            )

    else:

        form = OrcamentoForm()

    return render(
        request,
        "core/orcamento_form.html",
        {
            "form": form
        }
    )

@login_required
def editar_orcamento(request, id):

    orcamento = get_object_or_404(
        Orcamento,
        id=id
    )

    if request.method == "POST":

        form = OrcamentoForm(
            request.POST,
            instance=orcamento
        )

        if form.is_valid():

            form.save()

            messages.success(
            request,
            "Orçamento atualizado com sucesso!"
            )

            return redirect("/orcamentos/")

    else:

        form = OrcamentoForm(
            instance=orcamento
        )

    return render(
        request,
        "core/orcamento_form.html",
        {
            "form": form
        }
    )

@login_required
def excluir_orcamento(request, id):

    orcamento = get_object_or_404(
        Orcamento,
        id=id
    )

    orcamento.delete()

    messages.success(
    request,
    "Orçamento excluído com sucesso!"
    )

    return redirect("orcamentos")

@login_required
def detalhe_orcamento(request, id):

    orcamento = get_object_or_404(
        Orcamento,
        id=id
    )

    return render(
        request,
        "core/orcamento_detalhe.html",
        {
            "orcamento": orcamento
        }
    )


@login_required
def orcamentos(request):

    orcamentos = Orcamento.objects.all()

    for o in orcamentos:
        print("========")
        print("Peça:", o.nome_peca)
        print("Material:", o.custo_material)
        print("Máquina:", o.custo_maquina)
        print("Energia:", o.custo_energia)
        print("Mão obra:", o.custo_mao_obra)

    return render(
        request,
        "core/orcamentos.html",
        {
            "orcamentos": orcamentos
        }
    )

@login_required
def configuracao_custo(request):

    configuracao = ConfiguracaoCusto.objects.first()

    if configuracao:
        form = ConfiguracaoCustoForm(
            request.POST or None,
            instance=configuracao
        )
    else:
        form = ConfiguracaoCustoForm(
            request.POST or None
        )

    if form.is_valid():
        form.save()
        return redirect("configuracao_custo")

    return render(
        request,
        "core/configuracao_custo_form.html",
        {
            "form": form
        }
    )

