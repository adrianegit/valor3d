from decimal import Decimal
from django.db import models

class Material(models.Model):
    nome = models.CharField(max_length=100)
    marca = models.CharField(max_length=100)
    tipo = models.CharField(max_length=50)

    peso_rolo = models.DecimalField(
        "Peso do rolo (g)",
        max_digits=8,
        decimal_places=2
    )

    valor = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    class Meta:
        verbose_name = "Material"
        verbose_name_plural = "Materiais"

    def __str__(self):
        return self.nome

class Impressora(models.Model):
    nome = models.CharField(max_length=100)
    marca = models.CharField(max_length=100)
    modelo = models.CharField(max_length=100)

     # 👇 NOVO CAMPO
    imagem = models.ImageField(upload_to='impressoras/', blank=True, null=True)

    potencia_watts = models.DecimalField(
        max_digits=8,
        decimal_places=2
    )

    valor_equipamento = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    vida_util_horas = models.PositiveIntegerField()

    ativa = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Impressora"
        verbose_name_plural = "Impressoras"

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

    class Meta:
        verbose_name = "Configuração de custo"
        verbose_name_plural = "Configurações de custo"

    def __str__(self):
        return "Configuração de custo"


class Orcamento(models.Model):

    STATUS_CHOICES = [
        ("novo", "Novo"),
        ("analise", "Em análise"),
        ("aprovado", "Aprovado"),
        ("producao", "Em produção"),
        ("finalizado", "Finalizado"),
        ("cancelado", "Cancelado"),
    ]

    status = models.CharField(
    max_length=20,
    choices=STATUS_CHOICES,
    default="novo",
    verbose_name="Status"
    )

    nome_peca = models.CharField(
        max_length=150,
        verbose_name="Nome da peça"
    )

    cliente = models.CharField(
        max_length=150,
        blank=True,
        verbose_name="Cliente"
    )

    observacoes = models.TextField(
        blank=True,
        verbose_name="Observações"
    )

    material = models.ForeignKey(
    Material,
    on_delete=models.CASCADE,
    verbose_name="Material"
    )

    impressora = models.ForeignKey(
    Impressora,
    on_delete=models.CASCADE,
    verbose_name="Impressora"
    )

    peso_peca = models.DecimalField(
        max_digits=8,
        decimal_places=2
    )

    tempo_impressao_horas = models.DecimalField(
        max_digits=8,
        decimal_places=2
    )

    tempo_mao_obra = models.DecimalField(
    max_digits=4,
    decimal_places=2,
    default=1.00,
    verbose_name="Tempo de mão de obra (horas)"
    )

    quantidade = models.PositiveIntegerField(
    default=1,
    verbose_name="Quantidade"
    )

    # ==========================================================
# Snapshot dos custos utilizados no orçamento
# ==========================================================

    valor_material_utilizado = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=True,
        blank=True,
        verbose_name="Valor do material utilizado"
    )

    valor_kwh_utilizado = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        null=True,
        blank=True,
        verbose_name="Valor do kWh utilizado"
    )

    custo_mao_obra_hora_utilizado = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        null=True,
        blank=True,
        verbose_name="Custo da mão de obra utilizado"
    )

    margem_lucro_utilizada = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        null=True,
        blank=True,
        verbose_name="Margem de lucro utilizada"
    )
    
    data_criacao = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:
        ordering = ["-data_criacao"]
        verbose_name = "Orçamento"
        verbose_name_plural = "Orçamentos"

    def __str__(self):
            return f"{self.nome_peca} - {self.material.nome}"
    
    @property
    def custo_material(self):

        valor_material = (
            self.valor_material_utilizado
            if self.valor_material_utilizado is not None
            else self.material.valor
        )

        custo_grama = (
            valor_material /
            self.material.peso_rolo
        )

        return (
            self.peso_peca *
            custo_grama *
            self.quantidade
        ).quantize(Decimal("0.01"))

    @property
    def custo_maquina(self):

        custo_hora = (
            self.impressora.valor_equipamento /
            self.impressora.vida_util_horas
        )

        return (
            self.tempo_impressao_horas *
            custo_hora
        ).quantize(Decimal("0.01"))
    
    @property
    def custo_energia(self):

        config = ConfiguracaoCusto.objects.first()

        valor_kwh = (
            self.valor_kwh_utilizado
            if self.valor_kwh_utilizado is not None
            else (
                config.valor_kwh if config else Decimal("0.00")
            )
        )

        potencia_kw = (
            self.impressora.potencia_watts /
            Decimal("1000")
        )

        consumo = (
            potencia_kw *
            self.tempo_impressao_horas
        )

        return (
            consumo *
            valor_kwh
        ).quantize(Decimal("0.01"))
    
    @property
    def custo_mao_obra(self):

        config = ConfiguracaoCusto.objects.first()

        valor_mao_obra = (
            self.custo_mao_obra_hora_utilizado
            if self.custo_mao_obra_hora_utilizado is not None
            else (
                config.custo_mao_obra_hora if config else Decimal("0.00")
            )
        )

        return (
            self.tempo_mao_obra *
            valor_mao_obra
        ).quantize(Decimal("0.01"))

    @property
    def custo_total(self):

        total = (
        self.custo_material +
        self.custo_maquina +
        self.custo_energia +
        self.custo_mao_obra
        )

        return total.quantize(Decimal("0.01"))
    
    @property
    def preco_com_lucro(self):

        config = ConfiguracaoCusto.objects.first()

        margem = (
            self.margem_lucro_utilizada
            if self.margem_lucro_utilizada is not None
            else (
                config.margem_lucro if config else Decimal("0.00")
            )
        )

        lucro = (
            self.custo_total *
            (margem / Decimal("100"))
        )

        return (
            self.custo_total + lucro
        ).quantize(Decimal("0.01"))

    @property
    def lucro(self):

        return (
        self.preco_com_lucro -
        self.custo_total
    ).quantize(Decimal("0.01"))