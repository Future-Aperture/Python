opcao = "s"
total = count = 0
listaItens = listaPrecos = []

while opcao == "s":

    print("-+" * 15)
    preco = float(input("\nPreço:\n> R$ "))
    nome = input("Nome do produto:\n> ").title()
    print("")
    print("-+" * 15)

    listaItens.append(nome)
    listaPrecos.append(preco)

    total += preco

    if preco > 1000:
        count += 1

    print("")
    opcao = input("Você deseja contiuar?\n> ")

index = listaPrecos.index(min(listaPrecos))

print(f'''
O produto mais barato da lista é o {listaItens[index]}, que está custando {min(listaPrecos):.2f}.
Há {count} produtos que custam mais de R$ 1000.
No total, foram gastos R$ {total:.2f}.
''')