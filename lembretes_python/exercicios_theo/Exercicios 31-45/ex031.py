#   ate 200km de viagem 0,50
#   0.45 para mais longas

viagem = float(input('Quantos quantos km sua viagem dura para eu calcular o valor: '))

if viagem > 200:
    print(f'O custo de sua viagem será R${viagem * 0.45:.2f}')

else: 
    print(f'O custo de sua viagem será R${viagem * 0.50:.2f}')