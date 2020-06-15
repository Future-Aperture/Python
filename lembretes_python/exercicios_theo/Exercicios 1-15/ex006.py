#   dobro triplo raiz


print('')

numero = int(input('Digite um número e veja seu dobro, triplo e raiz quadrada: '))

print(f'''
Seu número: {numero}
Dobro: {numero * 2}
triplo: {numero * 3}
Raiz quadrada: {numero / round(numero ** (1/2), 2)}
''')
