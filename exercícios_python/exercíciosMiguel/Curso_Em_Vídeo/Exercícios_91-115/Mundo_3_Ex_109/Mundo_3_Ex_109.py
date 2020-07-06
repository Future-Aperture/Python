import moeda

num = float(input("Digite um valor:\n>R$ "))

aumento = moeda.aumentar(num, format = True)
diminuido = moeda.diminuir(num, format = True)

print(f"\nAumentando {aumento[1]}%, temos {aumento[0]}")
print(f"Diminuindo {diminuido[1]}%, temos {diminuido[0]}")
print(f"\nO dobro de {moeda.moeda(num)} é {moeda.dobro(num, format = True)}")
print(f"A metade de {moeda.moeda(num)} é {moeda.metade(num, format = True)}")