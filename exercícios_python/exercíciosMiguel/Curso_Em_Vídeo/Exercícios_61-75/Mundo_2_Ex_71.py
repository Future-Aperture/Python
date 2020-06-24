money = int(input("Digite o valor que deseja sacar:\n> R$ "))
print("")

c50 = c20 = c10 = c1 = 0

while True:
    while money > 50:
        money -= 50
        c50 += 1
    print(f"Total de {c50} cédulas de R$ 50")

    while money > 20:
        money -= 20
        c20 += 1
    print(f"Total de {c20} cédulas de R$ 20")

    while money > 10:
        money -= 10
        c10 += 1
    print(f"Total de {c10} cédulas de R$ 10")

    while money >= 1:
        money -= 1
        c1 += 1
    print(f"Total de {c1} moedas de R$ 1")
    break