from random import randint

jogos = []
numeros = []
num = 1

print("-+" * 15)
quantidade = int(input("Quantos jogos deseja gerar?\n> "))
print("-+" * 15)

for i in range(0, quantidade):
    for k in range(0, 6):
        numeros.append(randint(1, 60))

    jogos.append(numeros[:])
    numeros.clear()

print()
print("-+" * 5, f"Sorteando {quantidade} Jogos", "-+" * 5)
for j in jogos:
    print(f"Jogo {num}: {j}")
    num += 1