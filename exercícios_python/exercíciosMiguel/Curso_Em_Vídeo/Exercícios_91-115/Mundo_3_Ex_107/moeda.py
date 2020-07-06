from random import randint

def metade(valor):
    return valor / 2

def dobro(valor):
    return valor * 2

def aumentar(valor):
    rng = randint(1, 100)
    return valor * (1 + (rng / 100)), rng

def diminuir(valor):
    rng = randint(1, 100)
    return valor - (valor * (rng / 100)), rng