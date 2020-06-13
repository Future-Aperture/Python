casa = float(input('Valor da casa: '))
salario = float(input('Salário: '))
anos = int(input('Em quantos anos deseja pagar? '))
prestacao = casa / (anos * 12)
minimo = salario * 30 / 100

if prestacao <= minimo:
    print('Emprestimo concedido!')

else:
    print('Emprestimo negado!')

