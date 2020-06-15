# calcule a soma entre todos os números que são múltiplos de três, ímpares
# que se encontram no intervalo de 1 até 500.

soma = 0

for numeros in range(1, 501, 2):
    if numeros % 3 == 0:
        soma = soma + numeros

print(f'\nA soma de todos os {numeros} numeros é {soma}')
        

