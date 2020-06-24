from datetime import date # Para poder ver o ano atual

#Cria o dicionario, e pede o nome, ano de nascimento e número da carteira de trabalho
ficha = {}
ficha["Nome"] = input("Nome: ").title()
ficha["Idade"] = date.today().year - int(input("Ano de nascimento: ")) # Faz o cálculo da idade
ficha["Ctps"] = int(input("Carteira de Trabalho ['0' caso n tenha]: "))

# Verifica se tiver ctps e pede pelo salário, ano de contrato e calcula a aposentdoria
if ficha["Ctps"] > 0:
    ficha["Contratação"] = int(input("Ano de contratação: "))
    ficha["Salário"] = float(input("Salário: R$ "))
    ficha["Aposentadoria"] = ficha["Idade"] + (35 - (date.today().year - ficha["Contratação"])) # Calcula a idade de aposentadoria

print()

#Dá um print em tudo
for i, j in ficha.items():
    print(f"    - {i}: {j}")