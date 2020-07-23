# criar um menu

def titulo(msg):
    print('-'*30)
    print(f'{msg:^30}')
    print('-'*30)


def menu():
    titulo('MENU')
    print('''  
1 - Ver pessoas cadastradas
2 - Cadastrar nova pessoa
3 - Sair do sistema
''')


menu()
print('-'*30)

while True:
    try:
        opção = int(input('Sua opção:\n> '))

    except:
        print('VALOR INVÁLIDO.')

    else:
        print(f'O valor digitado foi {opção}') 
        pass

    if opção == 1:
        titulo('OPÇÃO 1')
        
    if opção == 2:
        titulo('OPÇÃO 2')

    if opção == 3:
        titulo('OPÇÃO 3')
        print('Saindo do programa, tchau arrombado.')
        break