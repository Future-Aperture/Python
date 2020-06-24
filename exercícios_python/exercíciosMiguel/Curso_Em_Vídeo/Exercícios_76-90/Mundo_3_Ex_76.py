lista = ("Luvas", 25.90, "Camisetas", 35.90, "Lápis", 1.50, "Borracha", 2.50, "Teclado", 59.90, "Celular Xiaomi", 1400.00)

for i in range(0, len(lista)):
    if i % 2 == 0:
       print(f"{lista[i]:.<30}", end = "")
    else:
        print(f"R$ {lista[i]:.2f}")