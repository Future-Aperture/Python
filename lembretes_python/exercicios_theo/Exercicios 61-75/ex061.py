#   exercicio 51 so que com o while

print('-='*20, )
print('Contador de uma P.A ')
print('-='*20, )


primeiroTermo = int(input('\nDigite o primeiro termo:\n> '))
razao = int(input('A razão:\n> '))

contador = 1

while contador <= 10:
    print(f'{primeiroTermo}', end=' ')
    contador += 1
    primeiroTermo += razao 
    
print('Acabaste rapazeada')