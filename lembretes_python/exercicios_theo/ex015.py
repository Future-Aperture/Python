#60 por dia 0.15 por km
from time import sleep

print('')
print('Olá, bem vindo!')
print('')

#   calculo dias
dias = int(input('Quantos dias você ficou com o carro? '))
sleep(0.35)
print('')

#   calculo kms
kms = float(input('Quantos kilômetros você andou? '))
print('')

#   calculo dos dois
calculo = 60 * dias + kms * 0.15 


print(f'O total a pagar é R$: {calculo}')