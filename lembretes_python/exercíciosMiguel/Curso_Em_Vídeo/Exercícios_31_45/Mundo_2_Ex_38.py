num1 = int(input("Digite o primeiro número inteiro: "))
num2 = int(input("Digite o segundo número inteiro: "))

if num1 > num2:
    print(f"\n{'-' * 15}\n\nO número {num1} é maior do que o número {num2}.")

elif num2 > num1:
    print(f"\n{'-' * 15}\n\nO número {num2} é maior do que o número {num1}.")

else:
    print(f"\n{'-' * 15}\n\nOs números {num1} são iguais.")
