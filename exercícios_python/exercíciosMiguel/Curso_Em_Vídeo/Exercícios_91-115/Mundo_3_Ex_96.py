# Calcula a área
def area(largura, altura):
    return largura * altura

# Cria as linhas bonitinhas
def lin():
    print("-=" * 15)


lin()
print(f'{"Controle de Terrenos":>5}')
lin()

# Input da altura e da largura
larg = float(input("Digite a largura em metros:\n> "))
altu = float(input("Digite a altura em metros:\n> "))

lin()

# Output
print(f"A área total é {round(area(larg, altu), 2):.2f} m².")