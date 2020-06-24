from time import sleep

opcao = 0

num1 = int(input("Insira o primeiro valor inteiro: "))
num2 = int(input("Insira o segundo valor inteiro: "))
numeros = [num1, num2]

while opcao != 5:
    opcao = int(input("""
Insira a operação que deseja realizar:
1. Soma
2. Multiplicação
3. Comparar qual é o Maior

4. Novos Números
5. Sair
> """))

    if opcao == 1:
        print(f"\nO resultado da soma dos números {num1} e {num2} é: {num1 + num2}.")

    elif opcao == 2:
        print(f"\nO resultado da multiplicação dos números {num1} e {num2} é: {num1 * num2}.")

    elif opcao == 3:
        if num1 == num2:
            print(f"\nOs dois números {num1} são iguais.")
        else:
            print(f"\nDos números {num1} e {num2}, o maior deles é {max(numeros)}")

    elif opcao == 4:
            num1 = int(input("\nInsira o primeiro valor inteiro: "))
            num2 = int(input("Insira o segundo valor inteiro: "))
            numeros = [num1, num2]

    elif opcao == 5:
        print("\nSaindo", end = "")
        for i in range(0,3):
            sleep(0.3)
            print(".", end = "")
        break

    else:
        print("\nOpção inválida, tente novamente.")