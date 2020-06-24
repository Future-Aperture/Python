print('-='*30)
print('JOJO ROLL THE WEED')
print('-='*30)


contador = 0
lista = [ ]
numero5 = bool()

while True:
    numeros = int(input('\nDigite um número: '))
    resposta = str(input('Deseja continuar?[S/N] ')).strip()
    contador += 1
    lista.append(numeros)

    if resposta not in 'Ss':
        print('Obrigado.')
        break

if 5 in lista:
    numero5 = True


print(f'''
O total de números digitados: {contador}
Números em forma decrescente: {sorted(lista, reverse= True)}
valor 5: {numero5}''')

