matriz = [[None, None, None],
          [None, None, None],
          [None, None, None]]

for i in range(0, 3):
    for j in range(0, 3):
        valor = input(f"O que deseja colocar na posição {i}, {j}?\n> ")

        matriz[i][j] = valor

for i in range(0, 3):
    for j in range(0, 3):
        print(f"[{matriz[i][j]:^3}]", end = " ")
    print()