sexo = ""

sexo = input("Digite os seu sexo [M/F]:\n> ").lower()

while sexo not in "fm":
    sexo = input("\nOpção invalida, tente novamente.\nDigite os seu sexo [M/F]:\n> ").lower()

if sexo == "f":
    sexo = "feminino"
else:
    sexo = "masculino"

print("-+" * 15)
print(f"\nVocê é uma pessoa do sexo {sexo}.")