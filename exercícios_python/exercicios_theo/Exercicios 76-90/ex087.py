matriz = [[None, None, None],
          [None, None, None],
          [None, None, None]]

somaPar = somaTerceiraColuna = 0

for i in range(0, 3):
    for j in range(0, 3):
        valor = int(input(f"Que número deseja colocar na posição {i}, {j}?\n> "))

        if valor % 2 == 0:
            somaPar += valor
        
        if j == 2:
            somaTerceiraColuna += valor

        matriz[i][j] = valor

print()
for i in range(0, 3):
    for j in range(0, 3):
        print(f"[{matriz[i][j]:^3}]", end = " ")
    print()

print(f"\nA soma dos valores pares é: {somaPar}.")
print(f"A soma dos valores da terceira coluna: {somaTerceiraColuna}.")
print(f"O maior valor da segunda linha é: {max(matriz[1])}.")