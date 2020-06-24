#   jogo adivinhação
#   comp = numero random 0 - 5
from time import sleep
import random

print('')

computador = random.randint(0, 5)
#   variavel numero aleatorio

print('Vou pensar em um número de 0 a 5')
print('')
sleep(0.2)

print('Tente adivinhar, humano desprezível.')
print('')
sleep(0.5)

jogador = int(input('Sua tentativa: '))
#   variavel jogador

if jogador == computador:
    print('Você ganhou de mim, mero humano, não se acostume.')

else:
    print(f'Sucumba, humano desprezível, Eu ganhei, escolhi {computador}')