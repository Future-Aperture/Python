# Randomizador de numeros
from random import randint

# Função somar os valores pares de uma lista
def somarPar(ls):
    soma = 0

    # Verifica se o numero é par
    for j in ls:
        if j % 2 == 0:
            soma += j
    
    #Output 
    print(f"A soma dos números pares sorteados é: {soma}.")

# Função para sortear os numeros 
def sortear():
    listaSorteio = []

    # Faz o sorteio e coloca em uma lista
    for i in range(0, 5):
        listaSorteio.append(randint(0, 10))

    #Output
    print(f"Os 5 números sorteados foram: {listaSorteio}.")
    return listaSorteio


# Executa as funções
lista = sortear()
somarPar(lista)