matriz = [ [0, 0, 0], [0, 0, 0], [0, 0, 0] ]

for c in range(0, 3):
    for i in range(0, 3):
        matriz[c][i] = int(input(f'Digite um valor para [{c}], [{i}]: '))


print('-='*40)
print(matriz)
for c in range(0, 3):
    for i in range(0, 3):
        print(f'[{matriz[c][i]:^3}]',end=' ')
    print()