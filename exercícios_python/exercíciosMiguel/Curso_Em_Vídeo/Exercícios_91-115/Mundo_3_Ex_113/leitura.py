def leiaInt():
    while True:

        #Input
        num = input("Digite um número inteiro:\n> ")
        
        try:
            return int(num)

        except ValueError:
            print("\nO valor é possivel usar strings/floats, tente novamente.\n")

        except Exception as erro:
            print(erro.__class__)

def leiaFloat():
    while True:

        #Input
        num = input("Digite um número real:\n> ")
        
        try:
            return float(num)

        except ValueError:
            print("\nO valor é possivel usar strings, tente novamente.\n")

        except Exception as erro:
            print(erro.__class__)