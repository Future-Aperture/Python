opcao = "s"
count = 0
numeros = []
soma = 0

while opcao != "n":
    if opcao == "s":
        num = int(input("\nDigite um número: "))
        numeros.append(num)
        count += 1
        soma += num

    opcao = input("\nVocê deseja continuar? (S/N)\n> ").lower()
    
print(f'''\nVocê digitou {count} números, e a média deles é {soma / count:.2f}.
O maior número digitado foi {max(numeros)} e o menor foi {min(numeros)}.''')