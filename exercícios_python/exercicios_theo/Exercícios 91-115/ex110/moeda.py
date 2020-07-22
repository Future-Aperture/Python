
def aumento(p, taxa, formato=False):
    res = p + (p * taxa/100)
    return res if format is False else moeda(res)

def metade(p, formato=False):
    res = p/2
    return res if format is False else moeda(res)

def dobro(p, format=False):
    res = p * 2
    return res if format is False else moeda(res)


def moeda(p=0, moeda='R$', formato=False):
    return f'{moeda}{p:.2f}'.replace('.', ',') 

def resumo(p=0,taxa=5 ):
    print('-'*30)
    print('Resumo do valor:')
    print(f'Preço analisado: {moeda(p)}')
    print(f'Dobro do preço: {moeda(dobro(p, True))}')
    print(f'Metade do preço: {moeda(metade(p, True))}')
    print(f'Com {taxa} taxa de aumento: {aumento, taxa, True}')
    print('-'*30)