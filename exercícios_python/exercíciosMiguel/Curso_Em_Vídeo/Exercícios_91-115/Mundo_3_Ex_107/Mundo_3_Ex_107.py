import moeda

num = float(input("Digite um valor:\n>R$ "))

aumento = moeda.aumentar(num)
diminuido = moeda.diminuir(num)

print(f"\nAumentando {aumento[1]}% em R$ {num}, temos R$ {aumento[0]:.2f}")
print(f"Diminuindo {diminuido[1]}% em R$ {num}, temos R$ {diminuido[0]:.2f}")
print(f"\nO dobro de R$ {num:.2f} é R$ {moeda.dobro(num):.2f}")
print(f"A metade de R$ {num:.2f} é R$ {moeda.metade(num):.2f}")