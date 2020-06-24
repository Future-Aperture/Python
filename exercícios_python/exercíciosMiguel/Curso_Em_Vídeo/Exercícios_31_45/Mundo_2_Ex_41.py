from datetime import date

ano = int(input("Insira o ano de nascimento do atleta: "))

idade = date.today().year - ano

if idade <= 9:
    print(f"\nCom a idade de {idade}, você participará do campeonato MIRIM.")

elif idade > 9 and idade <= 14:
    print(f"\nCom a idade de {idade}, você participará do campeonato INFANTIL.")

elif idade > 14 and idade <= 19:
    print(f"\nCom a idade de {idade}, você participará do campeonato JÚNIOR.")

elif idade > 19 and idade <= 25:
    print(f"\nCom a idade de {idade}, você participará do campeonato SÊNIOR.")

else:
    print(f"\nCom a idade de {idade}, você participará do campeonato MASTER.")