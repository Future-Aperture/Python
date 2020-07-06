import moeda

num = float(input("Digite um valor:\n>R$ "))

aumento = moeda.aumentar(num)
diminuido = moeda.diminuir(num)

print(f"\nAumentando {aumento[1]}% em R$ {num}, temos {moeda.moeda(aumento[0])}")
print(f"Diminuindo {diminuido[1]}% em R$ {num}, temos {moeda.moeda(diminuido[0])}")
print(f"\nO dobro de {moeda.moeda(num)} é {moeda.moeda(moeda.dobro(num))}")
print(f"A metade de {moeda.moeda(num)} é {moeda.moeda(moeda.metade(num))}")