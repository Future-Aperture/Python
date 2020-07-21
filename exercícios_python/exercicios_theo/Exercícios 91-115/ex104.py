

def check(): # => função que checa se o que foi digitado realmente é um número
    while True:
        numero = input('Digite um número:')

        if numero.isnumeric():
            return int(numero)

        else:
            print('\nValor inválido.')
            



num = check()
print(f'Você digitou o valor {num}')