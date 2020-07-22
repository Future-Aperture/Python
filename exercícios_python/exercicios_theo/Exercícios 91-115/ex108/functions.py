# programa que importe módulos que:
# - aumente 10% | diminua pela metade | dobro do valor


def aumento(p, taxa):
    res = p + (p * taxa/100)
    return res

def metade(p):
    res = p/2
    return res

def dobro(p):
    res = p * 2
    return res


def moeda(preço=0, moeda='R$'):
    return f'{moeda}{preço:.2f}'.replace('.', ',')
