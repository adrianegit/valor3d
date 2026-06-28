from django import forms
from .models import Material


class MaterialForm(forms.ModelForm):

    class Meta:

        model = Material

        fields = [
            'nome',
            'marca',
            'tipo',
            'peso_rolo',
            'valor_rolo',
        ]