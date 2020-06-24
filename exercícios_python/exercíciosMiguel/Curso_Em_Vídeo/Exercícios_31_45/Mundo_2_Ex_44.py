valor = float(input('''Qual é o valor do produto a ser pago? 
> R$ '''))

print('''
Como deseja efetuar o pagamento? 

1. À Vista no Dinheiro / Cheque (10% OFF)
2. À Vista no Cartão (5% OFF)
3. 2x no Cartão
4. 3x no Cartão (20% JUROS)''')

print("-+-" * 15)

while True:

    pg = input("\n> ")

    if pg == '1':
        print(f"Vôce terá que pagar R$ {round(valor * 0.9, 2):.2f}.")
        break
    elif pg == '2':
        print(f"Você terá que pagar R$ {round(valor * 0.95, 2):.2f}.")
        break
    elif pg == '3':
        print(f"Você terá que pagar duas parcelas de R$ {round(valor / 2, 2):.2f}.")
        break
    elif pg == '4':
        print(f"Você terá que pagar três parcelas de R$ {round((valor * 1.20) / 3, 2):.2f}.")
        break
    else:
        print(f"{'-+-' * 15}\nOpção invalida, tente novamente.\n{'-+-' * 15}")