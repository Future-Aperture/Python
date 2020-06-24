from time import sleep
from random import randint


print('-='*20)
print('Jogo da adivinhação v2.0')
print('-='*20)
sleep(0.6)


# variaveis
cont = 0
computador = randint(0, 10)



print('\nEu pensei em um número de 0, 10. Tente adivinhá-lo.')

player = int(input('''\nQual seu chute?
> '''))
# tentativa do humano


while player != computador:
    dnv = str(input('''
Você errou. Deseja continuar? [S/N]
> ''')).strip().upper()

    if dnv in 'Ss':
        cont += 1 # Contagem de erros
        player = int(input('''
Outra tentativa:
> '''))

    else: 
        print(f'O número que eu pensei foi {computador}. Você é fraco.')
        break

print(f'Parabéns, você acertou em {cont} tentativas.')      