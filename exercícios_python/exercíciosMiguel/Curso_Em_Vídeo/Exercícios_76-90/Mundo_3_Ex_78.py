numeros = []

for i in range(0, 5):
    num = int(input(f"Digite um número inteiro na posição {i}:\n> "))

    numeros.append(num)

print(f"\nOs valores digitados foram {numeros}.")

print(f"O maior número digitado foi {max(numeros)} nas posições: ", end = "")
for l, m in enumerate(numeros):
    if m == max(numeros):
        print(l, end = "; ")

print(f"\nO menor número digitado foi {min(numeros)} nas posições: ", end = "")
for l, m in enumerate(numeros):
    if m == min(numeros):
        print(l, end = "; ")