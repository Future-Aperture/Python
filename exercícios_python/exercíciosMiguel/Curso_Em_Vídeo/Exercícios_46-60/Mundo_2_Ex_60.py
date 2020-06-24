num = int(input("Digite um número para saber seu fatorial:\n> "))
resultado = 1

print(f"{num}! = {num} ", end = "")

while num != 0:

    resultado *= num
    num -= 1

    print(f"x {num}" if num != 0 else "=", end = " ")

print(f"{resultado}")