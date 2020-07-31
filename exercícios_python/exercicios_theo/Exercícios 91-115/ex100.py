# => função que sorteie 5 numeros aleatorios
# => e outra que some os pares

from random import randint
from time import sleep



def linha():
    print('--'*20)
    
    
def sorteioNumeros(lista):
    print('Números gerados:')
    for contador in range (0,5):    
        contador = randint(0,15)    
        print(f'{contador}',end='-', flush=True)
        
        sleep(0.3)
        lista.append(contador)        
        
        
def somaPar(lista):   
    soma = 0     
    for pares in lista:
        if pares % 2 == 0:
            soma += pares
    print(f'\nSomando os valores {lista}, a soma de todos os pares são: {soma}')

   
input('\npressione enter para fechar.')
numeros = []  
sorteioNumeros(numeros)
somaPar(numeros)
