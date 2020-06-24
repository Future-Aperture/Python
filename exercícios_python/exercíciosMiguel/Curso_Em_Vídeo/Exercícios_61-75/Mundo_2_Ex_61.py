termo = int(input("Insira o primeiro termo:\n> "))
razao = int(input("Insira a razão:\n> "))
count = 0

print("")

while count != 10:
    print(f"{termo + (count * razao)}", end = " -> ")
    count += 1

print("...")