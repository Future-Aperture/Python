velocidade = int(input("Qual a velocidade do carro em Km/h? "))

if velocidade > 80:
    print(f'''
Você foi multado! O limite de velocidade é 80 Km/h.
Devido a está infralção, pagará uma multa de R$ {(velocidade - 80) * 7}.00!''')

else:
    print("\nTenha um bom dia, e digija com segurança.")