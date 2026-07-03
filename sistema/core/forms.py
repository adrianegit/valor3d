from django import forms

from .models import (
    Material,
    Impressora,
    Orcamento,
)


class MaterialForm(forms.ModelForm):

    class Meta:
        model = Material

        fields = [
            "nome",
            "marca",
            "tipo",
            "peso_rolo",
            "valor",
        ]


class ImpressoraForm(forms.ModelForm):

    class Meta:
        model = Impressora

        fields = [
            "nome",
            "marca",
            "modelo",
            "potencia_watts",
            "valor_equipamento",
            "vida_util_horas",
            "ativa",
        ]



class OrcamentoForm(forms.ModelForm):

    class Meta:
        model = Orcamento

        fields = [
            "material",
            "impressora",
            "peso_peca",
            "tempo_impressao_horas",
            "quantidade",
        ]

        labels = {
            "peso_peca": "Peso da peça (g)",
            "tempo_impressao_horas": "Tempo de impressão (h)",
            "quantidade": "Quantidade",
        }

        