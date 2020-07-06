from random import randint


def moeda(valor, moeda = "R$"):
    return f"{moeda} {valor:.2f}".replace(".", ",")


def metade(valor, format = False):
    if format:
        return moeda(valor / 2)

    return valor / 2


def dobro(valor, format = False):
    if format:
        return moeda(valor * 2)

    return valor * 2


def aumentar(valor, format = False):
    rng = randint(1, 100)

    if format:
        return moeda(valor * (1 + (rng / 100))), rng

    return valor * (1 + (rng / 100)), rng


def diminuir(valor, format = False):
    rng = randint(1, 100)

    if format:
        return moeda(valor - (valor * (rng / 100))), rng

    return valor - (valor * (rng / 100)), rng