

contador = 0
soma = 0


continuar = 's' or 'S'
media= 0

listaNum = [ ]


while continuar != 'N':
    numeros = int(input('\nDigite um número inteiro:\n>'))
    continuar = input('Deseja continuar[S/N]?\n> ').upper().strip()
    
    # coisas de lógica que sao chatas
    contador += 1
    soma += numeros
    media += numeros
    listaNum.append(numeros)

    if continuar != 'S': # pro programa parar
        break

media = media / contador

print(f'A média dos números é {media}')
print(f'O maior número foi {max(listaNum)} e o menor {min(listaNum)}.')
 
    

    
