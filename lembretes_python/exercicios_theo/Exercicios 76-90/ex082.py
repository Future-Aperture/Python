


valores = []
pares = [ ]
impares = [ ]


while True:
    numeros = int(input('\nDigite um número: '))
    resposta = str(input('Deseja continuar? [S/N]: '))
    valores.append(numeros) # adiciona todos os numeros na lista


    if numeros % 2 == 0: # numeros pares
        pares.append(numeros)
    
    else:
        impares.append(numeros)


    if resposta not in 'Ss': # caso nao queira continuar
        print('Obrigado.\n')
        break

print('-='*40)
print(f'''\n
Total da lista: {valores}
Lista dos ímpares: {impares}
Lista dos pares: {pares} ''') 

