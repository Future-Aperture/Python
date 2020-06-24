#   se ele vai se alistar, se precisa ou se ja passou do tempo
#   2020, pessoas de 2002 devem imediatamente
#   ESTOU NO ANO DE 2020

print('')

nascimento = int(input('Em qual ano você nasceu? '))
idade = 2020 - nascimento
print(' ')

if nascimento == 2002: #    imediatamente
    print('Você tem 18 anos, deve se alistar imediatamente')

elif nascimento < 2002: #   ja passou do tempo
    print(f'Você tem {idade} anos, deveria ter se alistado {idade - 18} anos atrás!!')

elif nascimento > 2002:
    print(f'Você tem {idade} anos, deve se alistar daqui a {18 - idade} anos')