
posicao = 0
lista = [ ]


for numero in range(0, 5):
    numeroS = int(input('\nDigite um número: '))

    
    if numero == 0:
        lista.append(numeroS)

    elif numero > lista[-1]:
        lista.append(numeroS)

    else: 
        posicao == 0
        while posicao < len(lista):
            if numero <= lista[posicao]:
                lista.insert(posicao, numeroS)
                break
            posicao += 1

    
print(f'Os números digitados em ordem são {lista}')