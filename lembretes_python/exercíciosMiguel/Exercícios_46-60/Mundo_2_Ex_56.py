nomes = []
idades = []
sexos = []
media = 0
mIdade = 0
mNome = ""
count = 0

for i in range(0, 4):
    print(f"----- {i + 1}° Pessoa -----")
    nome = input(f"Nome: ").title().strip()
    nomes.append(nome)

    idade = int(input(f"Idade: "))
    idades.append(idade)

    sexo = input(f"Sexo (M / F): ").lower().strip()
    sexos.append(sexo)

    media += idade

    if idade > mIdade and sexo == "m":
        mIdade = idade
        mNome = nome

    if sexo == "f" and idade < 20:
        count += 1

print(f'''
A média de idade do grupo é: {media / 4} anos.
O homem mais velho se chama {mNome} e tem {mIdade} anos.
Há {count} mulheres com menos de 20 anos.
''')