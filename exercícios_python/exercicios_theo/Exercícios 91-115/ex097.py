# => def ajuste = a linha ajustavel(pra n ficar dois prints em cima e embaixo)

def ajuste():
    print('-'*len(frase))


def linha():
    ajuste()
    print(frase) 
    ajuste()


frase = str(input('Digite a frase: ')).strip()
linha()
