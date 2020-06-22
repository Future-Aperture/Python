ficha = {}

ficha["Nome"] = input("Digite o nome do aluno:\n> ")
ficha["Média"] = float(input("Digite a média do aluno:\n> "))


if ficha["Média"] <= 5:
    ficha["Situação"] = "Recuperação"

elif ficha["Média"] > 7:
    ficha["Situação"] = "Aprovado"
    
else:
    ficha["Situação"] = "Reprovado"

print()

for i, j in ficha.items():
    print(f"{i}: {j}")