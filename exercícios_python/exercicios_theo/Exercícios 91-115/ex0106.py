
def titulo():
    print()
    print('='*23)
    print('Sistema de ajuda PyHelp')
    print('='*23)

titulo()
while True:
    comando = str(input('\nQual comando deseja receber ajuda?[Digite FIM para sair]\n> ')).lower()
    
    if comando == 'FIM':
        print('Obrigado!')
        break
    
    else:
        print('-'*40)
        print(f'Documentação do comando {comando}: ')
        print()
        help(comando)
        print('-'*40)

