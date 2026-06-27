from django.contrib import admin
from .models import Material, Impressora, ConfiguracaoCusto, Orcamento


@admin.register(Material)
class MaterialAdmin(admin.ModelAdmin):
    list_display = (
        "nome",
        "marca",
        "tipo",
        "peso_rolo",
        "valor_rolo",
    )

    search_fields = (
        "nome",
        "marca",
    )

    list_filter = (
        "tipo",
    )


@admin.register(Impressora)
class ImpressoraAdmin(admin.ModelAdmin):
    list_display = (
        "nome",
        "marca",
        "modelo",
        "potencia_watts",
        "valor_equipamento",
        "vida_util_horas",
    )

    search_fields = (
        "nome",
        "marca",
        "modelo",
    )


@admin.register(ConfiguracaoCusto)
class ConfiguracaoCustoAdmin(admin.ModelAdmin):
    list_display = (
        "valor_kwh",
        "custo_mao_obra_hora",
        "margem_lucro",
    )


@admin.register(Orcamento)
class OrcamentoAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "material",
        "impressora",
        "peso_peca",
        "tempo_impressao_horas",
        "quantidade",
        "custo_material",
        "custo_maquina",
        "custo_total",
        "data_criacao",
    )

    list_filter = (
        "material",
        "impressora",
        "data_criacao",
    )

    search_fields = (
        "id",
    )

    readonly_fields = (
        "data_criacao",
    )