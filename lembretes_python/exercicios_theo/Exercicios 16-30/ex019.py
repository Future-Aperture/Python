#   escolher aleatoriamente

import random
from time import sleep


lista = ['Gabriel', 'Arthur', 'Alexandre', 'Matheus', 'Joaquim']

print('')



print('NOMES DISPONÍVEIS: ')
print('')

for nome in lista: #    mostra os nomes disponiveis
    print(nome)

escolhido = random.choice(lista) # randomizer da lista



sleep(0.5)
print('')
print(f'O aluno escolhido foi {escolhido}')