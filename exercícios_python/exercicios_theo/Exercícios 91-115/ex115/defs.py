

def titulo(msg):
    print('-'*50)
    print(f'{msg:^50}')
    print('-'*50)

def menu():
    titulo('MENU')
    print('''  
1 - Ver pessoas cadastradas
2 - Cadastrar nova pessoa
3 - Sair do sistema
''')


def txt():
    arquivo = open('dados.txt', 'x') # => só cria o 'dados.txt'
    arquivo.close()


def escrever(nome, idade):
    arquivo = open('dados.txt', 'a+')

    arquivo.seek(0) # => faz o cursor ir pro começo do txt
    if len(arquivo.read(10)) > 0:
        arquivo.write('\n')
    
    arquivo.write(f'{nome};{idade}')
    arquivo.close()

def ler():
    arquivo = open('dados.txt', 'r+')

    linhas = arquivo.read().split('\n')
    for linha in linhas:
        linha = linha.split(';')

        print(f'nome: {linha[0]:<30}{linha[1]} anos',end='')
        print()
    print()
        
        
    arquivo.close()