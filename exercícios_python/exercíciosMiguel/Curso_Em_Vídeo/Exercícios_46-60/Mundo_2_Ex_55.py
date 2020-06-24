lista = []

for i in range(0, 5):
    kg = float(input(f"Insira o peso da {i + 1}° pessoa em kg:\n> "))
    lista.append(kg)

print(f"\nO menor peso da lista é: {min(lista)} kg\nJá o maior é: {max(lista)} kg")