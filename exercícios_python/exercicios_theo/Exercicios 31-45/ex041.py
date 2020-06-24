from datetime import date

#   9 anos: mirim
#   14 anos: infantil
#   19 anos: junior
#   25 anos: senior
#   25 anos: master

print('')

#   data de nascimento e cálculo da idade
ano = int(input("Insira o ano de nascimento do atleta: "))
idade = date.today().year - ano
print('')

if idade <= 9:
    print('Este atleta é classificado como MIRIM ')


elif idade >= 9 and idade <= 14:
    print('Este atleta é classificado como INFANTIL')


elif idade >= 14 and idade <= 19:
    print('Este atleta é classificado como JÚNIOR')

elif idade >= 19 and idade <= 25:
    print('Este atleta é classificado como SÊNIOR')

elif idade >= 25:
    print('Este atleta é considerado como MASTER')

