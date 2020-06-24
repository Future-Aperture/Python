limite = int(input("Digite quantos termos deseja ver:\n> "))

count = 0
x1, x2 = 0, 1

print(f"\n{x1} -> {x2}", end = " -> ")

while count < limite - 2:
    x3 = x1 + x2
    x1 = x2
    x2 = x3
    count += 1
    print(x3, end = " -> ")

print("...")