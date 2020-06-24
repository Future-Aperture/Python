pessoas = []
humano = []
opcao = "s"
maior = menor = 0


while opcao != "n":
    humano.append(input("Digite o nome da pessoa:\n> ").title())
    humano.append(float(input("Digite o peso da pessoa:\n> ")))

    if len(pessoas) == 0:
        maior = menor = humano[1]
    
    if humano[1] > maior:
        maior = humano[1]
    elif humano[1] < menor:
        menor = humano[1]

    pessoas.append(humano[:])
    humano.clear()
    
    opcao = input("Você deseja continuar? [S/N]\n> ").lower()

    if not opcao in "sn":
        print("Opção invalida, agora escreve tudo desde o começo.... otário.")
        break

print(f"\nForam cadastradas {len(pessoas)} pessoas.", end = "")
print(f"O maior peso foi {maior}kg, das pessoas: ")
for i in range(0, len(pessoas)):
    if pessoas[i][1] == maior:
        print(pessoas[i][0], end = " ")

print(f"\nO menor peso foi {menor} kg, das pessoas: ", end = "")
for i in range(0, len(pessoas)):
    if pessoas[i][1] == menor:
        print(pessoas[i][0], end = " ")