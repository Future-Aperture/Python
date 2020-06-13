n = 0

for i in range(1, 7):
    s = int(input("Digite um número par: "))
    if s % 2 == 0:
        n += s

print(f"\nA soma de todos os digitos pares é: {n}")