


lista = [ ]


while True:
    numero = lista.append(int(input('\nDigite um número: ')))
    continuar = str(input('Deseja continuar? [S/N]:\n>')).strip().upper()
    
    if continuar in 'S': # se for sim repete tudo padrao programacao 
        numero = lista.append(int(input('Digite um número: ')))
        print('Número já digitado.')
        continuar = str(input('Deseja continuar? [S/N]:\n>')).strip().upper()

    elif not continuar in 'NS':
        print('Opção inválida. Tente novamente.\n>')
        continuar = str(input('Deseja continuar? [S/N]:\n>')).strip().upper()
    
    
    else: # caso digite 'n' de primeira
        break
        


print(f'Os números digitados foram {sorted(lista)}')