from django import forms

from .models import (
    Material,
    Impressora,
    Orcamento,
    ConfiguracaoCusto,
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
            "nome_peca",
            "cliente",
            "observacoes",
            "status",
            "material",
            "impressora",
            "peso_peca",
            "tempo_impressao_horas",
            "quantidade",
        ]

        labels = {
            "nome_peca": "Nome da peça",
            "cliente": "Cliente",
            "observacoes": "Observações",
            "status": "Status",
            "material": "Material",
            "impressora": "Impressora",
            "peso_peca": "Peso da peça (g)",
            "tempo_impressao_horas": "Tempo de impressão (h)",
            "quantidade": "Quantidade",
        }

        widgets = {

            "nome_peca": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Ex: Suporte de celular"
            }),

            "cliente": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Nome do cliente"
            }),

            "observacoes": forms.Textarea(attrs={
                "class": "form-control",
                "rows": 3,
                "placeholder": "Detalhes da peça..."
            }),

            "status": forms.Select(attrs={
                "class": "form-select"
            }),

            "material": forms.Select(attrs={
                "class": "form-select"
            }),

            "impressora": forms.Select(attrs={
                "class": "form-select"
            }),

            "peso_peca": forms.NumberInput(attrs={
                "class": "form-control",
                "step": "0.01"
            }),

            "tempo_impressao_horas": forms.NumberInput(attrs={
                "class": "form-control",
                "step": "0.01"
            }),

            "quantidade": forms.NumberInput(attrs={
                "class": "form-control",
                "min": "1"
            }),
        }

class ConfiguracaoCustoForm(forms.ModelForm):


    class Meta:
        model = ConfiguracaoCusto

        fields = [
            "valor_kwh",
            "custo_mao_obra_hora",
            "margem_lucro",
        ]

        labels = {
            "valor_kwh": "Valor do kWh (R$)",
            "custo_mao_obra_hora": "Mão de obra por hora (R$)",
            "margem_lucro": "Margem de lucro (%)",
        }

        widgets = {
            "valor_kwh": forms.NumberInput(attrs={
                "class": "form-control"
            }),
            "custo_mao_obra_hora": forms.NumberInput(attrs={
                "class": "form-control"
            }),
            "margem_lucro": forms.NumberInput(attrs={
                "class": "form-control"
            }),
        }