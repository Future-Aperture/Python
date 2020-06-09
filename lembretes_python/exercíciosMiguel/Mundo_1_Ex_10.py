reais = float(input("Insira o quantia em reais que você possui.\nR$ "))

print(f"Com R$ {reais:.2f}, você poderia comprar aproximadamente U$ {round(reais / 4.91, 2)}")