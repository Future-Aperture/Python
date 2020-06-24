


from datetime import date
ano = date.today().year

menores_idade = 0
maiores_idade = 0


for pessoas in range(0, 7):
    nascimento = int(input('Data de nascimento: '))

    idade = ano - nascimento


    if idade >= 18:
        maiores_idade += 1

    elif idade < 18:
        menores_idade += 1


print(f'O total de maiores de idade são {maiores_idade}') # maiores
print(f'E o total de menores de idade são {menores_idade}') #   menores