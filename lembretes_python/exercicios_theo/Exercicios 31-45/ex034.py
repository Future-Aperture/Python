#   aumento salarial
#   superiores a 1250,00 aumento de 10%
#   menores ou igual, aumento de 15%

print('') # espaço inicial

salario = float(input('Digite o salário do funcionário: '))

if salario > 1250: #    aumento de 10%
    print(f'Com aumento de 10%, o que era {salario}, fica {salario + (salario * 10 / 100):.2f}')

if salario <= 1250:
    print(f'Com aumento de 15%, o que antes era {salario}, agora fica {salario + (salario * 10 / 100):.2f}')

