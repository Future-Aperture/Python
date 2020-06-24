traço = '='*30, '='*30
print(traço[0])
print('LOJINHA DO SEU ZÉ')
print(traço[1])


produtos = None
preços = None


lista = 'Boné', 15.90, 'Teclado', 20.00, 'Mouse', 29.90           

produtos = (lista[::2])
preços = (lista[1::2])

print('')
print('='*40)
print(f'{"PREÇOS":^40}')
print('='*40)

for posicao in range(0, len(lista)):
    if posicao % 2 == 0:
        print(f'{lista[posicao]:.<20}', end='')

    else:
        print(f'{lista[posicao]:^10}')




#print(preços)
#print(produtos)
#print(tudo)