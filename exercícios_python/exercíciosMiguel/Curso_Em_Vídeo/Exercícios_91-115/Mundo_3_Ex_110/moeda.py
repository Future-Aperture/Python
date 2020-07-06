from random import randint

# Formata o money
def moeda(valor, moeda = "R$"):
    return f"{moeda} {valor:.2f}".replace(".", ",")

# Devolve medade do valor
def metade(valor, format = False):
    if format:
        return moeda(valor / 2)

    return valor / 2

# Devolve o dobro do valor
def dobro(valor, format = False):
    if format:
        return moeda(valor * 2)

    return valor * 2

# Aumenta o valor em x%
def aumentar(valor, format = False):
    rng = randint(1, 100)

    if format:
        return moeda(valor * (1 + (rng / 100))), rng

    return valor * (1 + (rng / 100)), rng

# Diminue o valor em x%
def diminuir(valor, format = False):
    rng = randint(1, 100)

    if format:
        return moeda(valor - (valor * (rng / 100))), rng

    return valor - (valor * (rng / 100)), rng

# Devolve todas as funções formatadas
def resumo(valor, fmt = True):
    aumento = aumentar(valor, format = fmt)
    diminuido = diminuir(valor, format = fmt)

    print(f"""
{'-=' * 20}
{'RESUMO DO VALOR'.center(40)}
{'-=' * 20}
Preço Analisado: \t{moeda(valor)}

Dobro do preço: \t{dobro(valor, format = fmt)}
Metade do preço: \t{metade(valor, format = fmt)}

Aumentando {aumento[1]}%: \t{aumento[0]}
Diminuindo {diminuido[1]}%: \t{diminuido[0]}
{'-=' * 20}
""")