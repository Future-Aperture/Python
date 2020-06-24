#   contar de tantos em tantos, exemplo: 1 - 3 - 5 - 7

primeiroTermo = int(input('Digite o primeiro termo: '))
razao = int(input('Razão: '))
decimo = primeiroTermo + (10) * razao

for comprimento in range(primeiroTermo, decimo, razao ):
    print(f'{comprimento}', end=' ')
