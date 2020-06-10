#   embaralhar nomes
import random
import time



print('')

print('Escolha de ordem de apresentação ')
time.sleep(0.5)



lista = ['T-Bone', 'Marcus', 'Sitara', 'Aiden']  # lista dos nomes

print('')
print('Nomes disponíveis: ')
print('')

for nome in lista:  # mostrar nomes disponiveiss
    print(nome)



random.shuffle(lista)


print('')
time.sleep(0.5)
print(f'A ordem de apresentação fica: {lista} ')