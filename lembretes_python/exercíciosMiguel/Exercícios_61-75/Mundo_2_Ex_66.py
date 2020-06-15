num, soma, count = 0, 0, 0

print("Digite o número '999' para parar o programa.\n")

while num != 999:
    num = int(input("Digite um número inteiro: "))
    if num == 999:
        break
    
    soma += num
    count += 1

print(f"\nVocê digitou {count} números, e\na soma total deles é: {soma}.")