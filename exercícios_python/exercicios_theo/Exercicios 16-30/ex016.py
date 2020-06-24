#   numero inteiro
from time import sleep
from math import trunc


print('')

numero = float(input('Digite um número para ver sua parte inteira: '))

sleep(0.5)


print(f'''
Numero digitado: {numero}

Parte inteira:{trunc(numero)} ''')

