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

    valor = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

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

    quantidade = models.PositiveIntegerField(
    default=1,
    verbose_name="Quantidade"
    )
    
    data_criacao = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:
        ordering = ["-data_criacao"]

    def __str__(self):
            return f"{self.nome_peca} - {self.material.nome}"
    
    @property
    def custo_material(self):

        custo_grama = (
        self.material.valor /
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
            self.tempo_impressao_horas * custo_hora
        ).quantize(Decimal("0.01"))
    
    @property
    def custo_energia(self):

        config = ConfiguracaoCusto.objects.first()

        if not config:
            return Decimal("0.00")

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
            config.valor_kwh
        ).quantize(Decimal("0.01"))
    
    @property
    def custo_mao_obra(self):

        config = ConfiguracaoCusto.objects.first()

        if not config:
            return Decimal("0.00")

        return (
            self.tempo_impressao_horas *
            config.custo_mao_obra_hora
        ).quantize(Decimal("0.01"))

    @property
    def custo_total(self):

        total_unitario = (
            self.custo_material +
            self.custo_maquina +
            self.custo_energia +
            self.custo_mao_obra
        )

        return (
            total_unitario * self.quantidade
        ).quantize(Decimal("0.01"))
    
    @property
    def preco_com_lucro(self):

        config = ConfiguracaoCusto.objects.first()

        if not config:
            return self.custo_total

        lucro = (
            self.custo_total *
            (config.margem_lucro / Decimal("100"))
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