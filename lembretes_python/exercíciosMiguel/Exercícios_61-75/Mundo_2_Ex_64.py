num, soma, count = 0, 0, 0

print("Digite o número '999' para parar o programa.\n")

num = int(input("Digite um número inteiro: "))

while num != 999:
    soma += num
    count += 1

    num = int(input("Digite um número inteiro: "))

print(f"\nVocê digitou {count} números, e\na soma total deles é: {soma}.")