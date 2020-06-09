#   aumento salarialkkk
from time import sleep


print('')
salario = float(input('Digite o salário do funcionário R$: '))

novo = salario +  (salario * 15 / 100)
sleep(0.5)

print('')
print(f'O novo salário do funcionário, com 15% de aumento, fica {float(novo)}')
