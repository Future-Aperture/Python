# Declarando as variaveis
opcao = "s"
humano = {}
pessoas = []
media = 0

while opcao != "n":
    # Input do nome, sexo e idade
    humano["nome"] = input("\nNome: \n> ").title()
    humano["idade"] = int(input("Idade: \n> "))
    humano["sexo"] = input("Sexo [M/F]: \n> ").upper()

    # Verifica se foi inserido o sexo correto
    while humano["sexo"] not in "MF":
        print("\nOpção invalida, tente usar apenas 'M' ou 'F'.")
        humano["sexo"] = input("Sexo [M/F]: \n> ").upper()

    pessoas.append(humano.copy())

    humano.clear()

    opcao = input("\nQuer continuar? [S/N]\n> ").lower()

    # Verifica se foi inserido SIM ou NÃO como opcao
    while not opcao in "sn":
        print("Opção invalida, tente usar apenas 'S' ou 'N'.")
        opcao = input("\nQuer continuar? [S/N]\n> ").lower()

# Calcula a média
for i in range(0, len(pessoas)):
    media += pessoas[i]["idade"] / len(pessoas)

# Output principal
print(f'''\nA. Ao todo temos {len(pessoas)} pessoas cadastradas.

B. A média de idade é de {round(media, 2):.2f} anos.

C. As mulheres cadastradas foram: ''', end = "")

# Pega só as mulheres
for j in pessoas:
    if j["sexo"] == "F":
        print(j["nome"], end = "; ")

print("\n\nD. Lista de pessoas que estão acima da média:")

# Pega só quem tá acima da média
for k in pessoas:
    if k["idade"] > media:
        print(f"Nome: {k['nome']}; Idade: {k['idade']}; Sexo: {k['sexo']}")