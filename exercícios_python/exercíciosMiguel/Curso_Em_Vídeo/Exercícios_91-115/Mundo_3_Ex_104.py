def leiaInt():
    while True:
        #Input
        msg = input("Digite um número:\n> ")
        
        #Verifica se é número
        if msg.isnumeric():
            return int(msg)

        else:
            print("\nValor invalido, tente novamente.\n")
            continue


# Output
num = leiaInt()
print(f"\nVocê digitou o número {num}.")