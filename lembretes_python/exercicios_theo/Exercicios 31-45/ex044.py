

print('')
print('=-'*20)
print('LOJINHA DO THEOZIN DO T.I')
print('=-'*20)



preço = float(input('''
Digite o preço do produto:
> R$: '''))
print('')

juros = preço + (preço * 20 / 100) #    preço com 20% de juros


pagamento = int(input( #    escolha da forma de pagamento


f'''
Digite a forma de pagamento:

[1] à vista dinheiro/cheque: 10% de desconto

[2] à vista no cartão: 5% de desconto

[3] em até 2x no cartão: preço formal 

[4] 3x  no cartão: 20% de juros

> '''))
print('')


if pagamento == 1:
    print(f'O valor de R${preço}, com um desconto de 10% aplicado, fica R${preço - (preço * 10 / 100):.2f}') # 10% desconto 

elif pagamento == 2:
    print(f'O valor de R${preço}, agora com 5% de desconto, fica R${preço - (preço * 10 / 100):.2f} ') # 5% desconto

elif pagamento == 3:
    print(f'O produto parcelado em 2x fica R${preço / 2:.2f} por mês')

else: 
    print(f'O produto fica R${juros}, dividido em 3x fica R${juros / 3:.2f} por mês.')