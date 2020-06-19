print('Digita um 3 ai namoral pq assim to cm preguiça de fazer uns if tlg')
numero = (int(input('\nDigite um número: ')), 
        int(input('Digite outro um número: ')),
        int(input('Digite mais um número: ')),
        int(input('Digite o último número: ')),)



numerosPares = [ ] # lista que os numeros pares vão


for par in numero:
    if par % 2 == 0: # variavel par serve so pra ver se o numero é par
        numerosPares.append(par)

print(f'''
O número '9' apareceu {numero.count(9)}x
O primeiro número 3 está na posição {numero.index(3) + 1}
Os números pares são: {numerosPares}

''')

