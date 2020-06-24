print('')


lista = []

for pessoas in range(0, 5):
    peso = float(input('Digite o peso: '))

    lista.append(peso)

print(f'''
O maior peso lido foi {max(lista)}
O menor peso lido foi {min(lista)}
''')
