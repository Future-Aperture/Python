

expressao = input('Digite a expressão numérica: ')

contador = expressao.count('(' and ')' ) # contagem de parenteses

if contador == expressao:
    print('Expressão válida.')

else:
    print('Expressão inválida.')