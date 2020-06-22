opcao = "s"
numeros = []

while opcao != "n":
    numeros.append(int(input("Digite um valor:\n> ")))
    opcao = input("Você deseja continuar? [S/N]\n> ").lower()

    if not opcao in "sn":
        print("Opção invalida, tente novamente.")

numeros.sort(reverse = True)

print(f'''
Foram digitados {len(numeros)} números.
A lista em ordem decrescente é: {numeros}
O número "5" apareceu {numeros.count(5)} vezes.''')