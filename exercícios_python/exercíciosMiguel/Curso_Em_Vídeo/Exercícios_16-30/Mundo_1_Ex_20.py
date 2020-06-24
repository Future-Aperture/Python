from random import randint

nomes = ["João", "Carlos", "Henrique", "Enzo", "Carla", "Maria Joaquina", "Mariana", "Théo", "Arthur", "Miguel", "Gabriel"]

print("A ordem de apresentação será: ")
for g in range(0, len(nomes) - 1):
    i = randint(0, len(nomes) - 1)
    print(nomes[i])
    del nomes[i]