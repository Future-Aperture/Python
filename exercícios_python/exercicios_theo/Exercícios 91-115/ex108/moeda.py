# programa que importe módulos que:
# - aumente 10% | diminua pela metade | dobro do valor

import functions


p = float(input('\nDigite um valor R$: '))
print('-'*30)
print(f'O valor de {functions.moeda(p)} mais 10% é: {functions.aumento(p, 10)}')
print(f'\nA metade de {functions.moeda(p)} é {functions.metade(p)}')
print(f'\nO dobro de {functions.moeda(p)} é {functions.dobro(p)} ')
print('-'*30)