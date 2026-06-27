from decimal import Decimal
from django.db import models


class Material(models.Model):
    nome = models.CharField(max_length=100)
    marca = models.CharField(max_length=100)
    tipo = models.CharField(max_length=50)

    peso_rolo = models.DecimalField(
        max_digits=8,
        decimal_places=2
    )

    valor_rolo = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    def __str__(self):
        return self.nome



class Impressora(models.Model):
    nome = models.CharField(max_length=100)
    marca = models.CharField(max_length=100)
    modelo = models.CharField(max_length=100)

    potencia_watts = models.DecimalField(
        max_digits=8,
        decimal_places=2
    )

    valor_equipamento = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    vida_util_horas = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    def __str__(self):
        return self.nome



class ConfiguracaoCusto(models.Model):
    valor_kwh = models.DecimalField(
        max_digits=8,
        decimal_places=2
    )

    custo_mao_obra_hora = models.DecimalField(
        max_digits=8,
        decimal_places=2
    )

    margem_lucro = models.DecimalField(
        max_digits=5,
        decimal_places=2
    )

    def __str__(self):
        return "Configuração de custo"



class Orcamento(models.Model):
    material = models.ForeignKey(
        Material,
        on_delete=models.CASCADE
    )

    impressora = models.ForeignKey(
        Impressora,
        on_delete=models.CASCADE
    )

    peso_peca = models.DecimalField(
        max_digits=8,
        decimal_places=2
    )

    tempo_impressao_horas = models.DecimalField(
        max_digits=8,
        decimal_places=2
    )

    quantidade = models.IntegerField(
        default=1
    )

    data_criacao = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"Orçamento {self.id}"


    @property
    def custo_material(self):

        custo_grama = (
            self.material.valor_rolo /
            self.material.peso_rolo
        )

        return self.peso_peca * custo_grama


    @property
    def custo_maquina(self):

        custo_hora = (
            self.impressora.valor_equipamento /
            self.impressora.vida_util_horas
        )

        return self.tempo_impressao_horas * custo_hora


    @property
    def custo_total(self):

        return (
            self.custo_material +
            self.custo_maquina
        )