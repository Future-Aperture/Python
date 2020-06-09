#Variavel *ponto*
ponto = 0

#Preço
preco = float(input("\nDigite o preço do produto: "))

if preco < 30:
    ponto += 1
elif preco < 120 and preco >= 30:
    ponto += 2
else:
    ponto += 3

#Vendas
venda = float(input("\nDigite a quantidade de vendas do produto: "))

if venda < 10:
    ponto += 1
elif venda < 100 and venda >= 10:
    ponto += 2
else:
    ponto += 3

#Estoque
estoque = float(input("\nDigite a quantidade de estoque do produto: "))

if estoque < 20:
    ponto += 1
elif estoque < 50 and estoque >= 20:
    ponto += 2
else:
    ponto += 3

#Define a categoria do produto
if ponto <= 4:
    print("\nEste produto é BROXA!")
elif ponto >= 8:
    print("\nEste produto é PICA!")
else:
    print("\nEste produto é MEIA-BOMBA!")