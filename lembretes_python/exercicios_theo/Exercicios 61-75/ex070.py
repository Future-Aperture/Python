print('-'*30)
print('   LOJINHAS THEOZIN DO T.I')
print('-'*30)

resposta = 's'
total = 0
maior1000 = 0
maisBarato = [ ]
nomeBarato = [ ]

while resposta not in 'Nn':

    # informaçoes do produto
    nome = str(input('\nDigite o nome do produto:\n>: '))
    preço = float(input('Digite o preço do produto:\n>R$ '))
    resposta = str(input('\nDeseja continuar[S/N]:\n> ')).strip().lower()
    total += preço

    if preço > 1000: # se é maior que 1000
        maior1000 += 1

    # joga o nome e o preço dos itens numa lista 
    nomeBarato.append(nome)
    maisBarato.append(preço)

print(f'''
O total da compra de todos os itens fica {total}
{maior1000}produtos custam mais de R$1000,00
{min(nomeBarato)} é o produto mais barato, e ele custa {max(maisBarato)} ''')