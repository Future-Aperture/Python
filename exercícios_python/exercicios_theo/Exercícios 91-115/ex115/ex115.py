from defs import txt, menu, escrever, titulo, ler


try:
    txt()

except:
    print('tente novamente')
    pass


print()
menu()
print('-'*50)


while True:
    try:
        opção = int(input('Sua opção:\n> '))

    except:
        print('VALOR INVÁLIDO.')


    if opção == 1:
        print()
        titulo('PESSOAS CADASTRADAS:')
        ler()

    if opção == 2:
        print()
        titulo('CADASTRO DE NOVA PESSOA:')
        nome = str(input('Digite o nome da pessoa: '))
        idade = int(input('Digite a idade da pessoa: '))
        print('-'*50)

        escrever(nome,idade)
    
    if opção == 3:
        titulo('Saindo do programa, flw e nois.')
        break
   
