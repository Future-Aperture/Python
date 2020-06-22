opcao = "s"
numeros = []
numerosImpares = []
numerosPares = []

while opcao != "n":
    numeros.append(int(input("Digite um valor:\n> ")))
    opcao = input("Você deseja continuar? [S/N]\n> ").lower()

    if not opcao in "sn":
        print("Opção invalida, tente novamente.")

for i in numeros:
    if i % 2 == 0:
        numerosPares.append(i)

    else:
        numerosImpares.append(i)

numeros.sort()
numerosImpares.sort()
numerosImpares.sort()

print(f'''
A lista de todos os números é:\n{numeros}

A lista dos numeros pares é:\n{numerosPares}

A lista dos numeros ímpares é:\n{numerosImpares}''')