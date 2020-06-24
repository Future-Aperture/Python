count = []

numeros = (int(input("Insira o primeiro número inteiro: ")),
int(input("Insira o segundo número inteiro: ")),
int(input("Insira o terceiro número inteiro: ")),
int(input("Insira o quarto número inteiro: ")))

for i in numeros:
    if i % 2 == 0:
        count.append(i)

print(f"\nOs valores digitados foram: {numeros}\n")

if 9 in numeros:
    print(f"O número '9' apareceu {numeros.count(9)} vezes.")
else:
    print("Não houve nenhum valor '9' digitado.")

if 3 in numeros:
    print(f"O número '3' apareceu pela primeira vez na posição {numeros.index(3) + 1}.")
else:
    print("Não houve nenhum valor '3' digitado.")

if count:
    print(f"Os números {count} são pares.")
else:
    print("Não houve nenhum valor par digitado.")