from math import modf


num = int(input("Digite um número inteiro: "))

print(f'''{"-" * 15}

1. Converter para Hexadecimal

2. Converter para Binário

3. Converter para Octal''')

while True: 
    choice = input("\nO que deseja fazer com esse número? ")

    if choice == "1":
        print(f'{"-" * 15}\nO número {num} em hexadecimal é: {hex(num)[2:]}')
        break

    elif choice == "2":
        print(f'{"-" * 15}\nO número {num} em binário é: {bin(num)[2:]}')
        break

    elif choice == "3":
        print(f'{"-" * 15}\nO número {num} em octal é: {oct(num)[2:]}')
        break

    else:
        print(f'{"-" * 15}\nOpção Invalida, tente novamente.\n')
        continue