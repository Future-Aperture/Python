opcao = "s"
qHomens = mulheresNovas = mais18 = 0

while opcao == "s":

    print("-+" * 15)
    idade = int(input("\nIdade:\n> "))
    sexo = input("Sexo (M/F):\n> ").lower()
    print("")
    print("-+" * 15)

    if idade > 18:
        mais18 += 1

    if sexo == "m":
        qHomens =+ 1

    if sexo == "f" and idade < 20:
        mulheresNovas += 1

    opcao = input("\nDeseja continuar? (S/N)\n> ").lower()
    print("")

print("-+" * 15)
print(f'''
Há {mais18} pessoas com mais de 18 anos.
Tivemos {qHomens} homens cadastrados.
Das mulheres, {mulheresNovas} tem menos de 20 anos.''')