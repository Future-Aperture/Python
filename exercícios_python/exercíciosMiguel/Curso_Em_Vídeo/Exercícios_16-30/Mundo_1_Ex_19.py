from random import randint

nomes = ["João", "Carlos", "Henrique", "Enzo", "Carla", "Maria Joaquina", "Mariana", "Théo", "Arthur", "Miguel", "Gabriel"]

for g in range(0, len(nomes) - 1):
    print(f"Aluno número {g + 1}: {nomes[g]}")

i = randint(0, len(nomes) - 1)

print(f"\nO(a) aluno(a) escolhido através do sorteio do professor, foi o número {i + 1}, ou seja, {nomes[i]}")