print()
print('-='*40)
print('ANÁLISE DE DADOS')
print('-='*40)
print()



contador = 0
temp = [ ]
dados = [ ] # lista 2D
maior = menor = 0

while True:
    temp.append(str(input('Digite o nome da pessoa:\n> ')))
    temp.append(float(input('Digite o peso:\n> ')))
    if len(dados) == 0: # se nao tiver ninguem na lista
        maior = menor = temp[1] # o primeiro peso é maior e menor ao mesmo tempo
    else:
        if temp[1] > maior:
            maior = temp[1]

        elif temp[1] < menor:
            menor = temp[1]

    resp = str(input('Deseha continuar?[S/N]:\n> '))
    contador += 1


    # adicionar os dados à lista
    dados.append(temp[:]) 
    temp.clear()

    if resp not in 'Ss':
        break

print(f'''
O total de pessoas cadastradas foram {contador}
O peso da pessoa mais pesada é {maior}
O peso da pessoa mais leve é {menor}
''')