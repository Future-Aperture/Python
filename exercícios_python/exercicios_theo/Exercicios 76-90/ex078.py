lista = [ ]

for numeros in range(6):
    lista.append(int(input('Digite um número inteiro: ')))
print(lista)

print(f'''

O maior número digitado foi {max(lista)} na posição {lista.index(max(lista)) + 1}
O menor número digitado foi {min(lista)} na posição {lista.index(min(lista)) + 1} 

''')


