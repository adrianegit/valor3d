def calcular_custo_material(peso_gramas, preco_kg):
    preco_grama = preco_kg / 1000
    return peso_gramas * preco_grama


def calcular_custo_energia(tempo_horas, consumo_watts, tarifa_kwh):
    consumo_kwh = (consumo_watts * tempo_horas) / 1000
    return consumo_kwh * tarifa_kwh


def calcular_custo_maquina(tempo_horas, custo_hora):
    return tempo_horas * custo_hora


def calcular_preco_final(custo_material, custo_energia, custo_maquina):
    return custo_material + custo_energia + custo_maquina


# ----------------------------
# Teste
# ----------------------------

material = calcular_custo_material(50, 120)

energia = calcular_custo_energia(
    tempo_horas=2,
    consumo_watts=120,
    tarifa_kwh=0.95
)

maquina = calcular_custo_maquina(
    tempo_horas=2,
    custo_hora=0.60
)

total = calcular_preco_final(
    material,
    energia,
    maquina
)

print(total)