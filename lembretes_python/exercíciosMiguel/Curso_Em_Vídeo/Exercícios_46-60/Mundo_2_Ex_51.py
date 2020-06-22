termo = int(input("Insira o primeiro termo:\n> "))
razao = int(input("Insira a razão:\n> "))

print("")

for i in range(termo, termo + 10 * razao, razao):
    print(f"{i}", end = " -> ")

print("...")