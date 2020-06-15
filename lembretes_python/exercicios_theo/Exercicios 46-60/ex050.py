#   6 numeros e mostre a soma dos pares

soma = 0

for numero in range(0, 6):
    par = int(input('Digite um número: '))
    if par % 2 == 0: #   se é par
        soma = soma + par

print(f'A soma dos número pares será de {soma}')
