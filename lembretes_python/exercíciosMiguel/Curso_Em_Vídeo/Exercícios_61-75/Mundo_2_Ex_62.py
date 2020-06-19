termo = int(input("Insira o primeiro termo:\n> "))
razao = int(input("Insira a razão:\n> "))
count = 0
limite = 10

print("")

while count < limite:
    print(f"{termo + (count * razao)}", end = " -> ")
    
    count += 1

    if limite == count:
        limite += int(input("...\n\nQuantos termos a mais você quer mostrar?\n> "))