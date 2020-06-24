ficha = []
opcao = "s"
num = index = 0

while opcao != "n":
    nome = input("Digite o nome do aluno: ").title()
    nota1 = float(input("Digite a primeira nota do aluno: "))
    nota2 = float(input("Digite a segunda nota do aluno: "))
    media = round((nota1 + nota2) / 2, 1)

    ficha.append([nome, [nota1, nota2], media])

    opcao = input("Deseja continuar? [S/N]\n> ")


print(f"\n{'N.°':<6}{'Nome':<15}Média")
for numero, item in enumerate(ficha):
    print(f"{numero:<6}{item[0]:<15}{item[2]}")

while index != 999:
    index = int(input("\nQual aluno deseja ver as notas? [999 para sair]\n> "))

    if index in range(0, len(ficha)):
        print(f"\nO aluno {ficha[index][0]} teve as notas {ficha[index][1]}.")