from django.contrib import admin

from .models import (
    Material,
    Impressora,
    ConfiguracaoCusto,
    Orcamento,
)



@admin.register(Material)
class MaterialAdmin(admin.ModelAdmin):
    list_display = (
        "nome",
        "marca",
        "tipo",
        "peso_rolo",
        "valor",
    )

    search_fields = ("nome", "marca")
    list_filter = ("tipo",)


@admin.register(Impressora)
class ImpressoraAdmin(admin.ModelAdmin):
    list_display = (
        "nome",
        "marca",
        "modelo",
        "potencia_watts",
        "valor_equipamento",
        "vida_util_horas",
        "ativa",
    )

    search_fields = (
        "nome",
        "marca",
        "modelo",
    )

    list_filter = ("ativa",)


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
        "custo_material_formatado",
        "custo_maquina_formatado",
        "custo_total_formatado",
        "data_criacao",
    )

    ordering = (
        "-data_criacao",
    )

    list_per_page = 20

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

    @admin.display(description="Custo Material")
    def custo_material_formatado(self, obj):
        return f"R$ {obj.custo_material:.2f}"

    @admin.display(description="Custo Máquina")
    def custo_maquina_formatado(self, obj):
        return f"R$ {obj.custo_maquina:.2f}"

    @admin.display(description="Custo Total")
    def custo_total_formatado(self, obj):
        return f"R$ {obj.custo_total:.2f}"



