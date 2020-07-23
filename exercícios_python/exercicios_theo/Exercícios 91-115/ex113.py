

def check(): # => função que checa se o que foi digitado realmente é um número
    while True:
        try:
            numero = int(input('Digite um número:\n> '))
            return numero

        except:
            print('\nValor inválido.')



def checkFloat(): # => função que checa se o que foi digitado realmente é um número
    while True:
        try:
            numero = float(input('Digite um número float:\n> '))
            return numero

        except:
            print('\nValor inválido.')
        

num = check()
numFloat = checkFloat()
print('-'*30)
print(f'\nVocê digitou o valor {num}')
print(f'Você digitou o número float: {numFloat}')
