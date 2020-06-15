lista = []

for i in range(0, 5):
    kg = float(input(f"Insira o peso da {i + 1}° pessoa em kg:\n> "))
    lista.append(kg)
    
lista.sort()

print(f"\nO menor peso da lista é: {lista[0]} kg\nJá o maior é: {lista[4]} kg")