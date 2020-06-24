#   tabuada

numero = int(input('\nDigite o numero que deseja ver a tabuada: '))

print('-='*10)

for tabuada in range(1, 11):
    print(f'{numero} X {tabuada} = {tabuada * numero}')

print('-='*10)