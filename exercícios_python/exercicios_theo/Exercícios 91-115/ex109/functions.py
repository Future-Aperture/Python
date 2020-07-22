# programa que importe módulos que:
# - aumente 10% | diminua pela metade | dobro do valor


def aumento(p, taxa, formato=False):
    res = p + (p * taxa/100)
    return res if format is False else moeda(res)

def metade(p, formato=False):
    res = p/2
    return res if format is False else moeda(res)

def dobro(p, format=False):
    res = p * 2
    return res if format is False else moeda(res)


def moeda(preço=0, moeda='R$', formato=False):
    return f'{moeda}{preço:.2f}'.replace('.', ',') 
