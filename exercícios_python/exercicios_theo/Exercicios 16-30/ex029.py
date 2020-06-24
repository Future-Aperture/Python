#   limite de 80km/h
#   R$7,00 por km acima do limite

print('')



velocidade = int(input('Velocidade do carro: ')) 


if velocidade > 80: #   if da multa
    print(f'''
    Multado! 
    
    Limite de velocidade: 80km/h
    
    Você passou a {velocidade}

    Será multado em R${(velocidade - 80) * 7}
    
    Tenha um bom dia!
    ''')