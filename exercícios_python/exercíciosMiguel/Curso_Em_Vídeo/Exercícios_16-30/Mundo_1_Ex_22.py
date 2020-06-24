name = input("Insira o seu nome completo: ")

print(f'''\nTudo maiúsculo: {name.upper()}
Tudo minúsculo: {name.lower()}

Quantas letras tem o nome inteiro: {len(name.replace(" ", ""))}
Quantas letras tem o primeiro nome: {len(name.split(" ")[0])}''')