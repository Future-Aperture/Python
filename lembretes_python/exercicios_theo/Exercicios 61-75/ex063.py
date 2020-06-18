
print('-'*30)
print('Sequência de Fibonacci')
print('-'*30)

contador = 1


termos = int(input('\nQuantos termos você quer ver?\n> '))

#   3 primeiros termos
t1 = 0
t2 = 1
cont = 3

print(f'{t1} - {t2}', end=' ')

while contador <= termos:
    t3 = t1 + t2
    t1 = t2
    t2 = t3  
    contador += 1
    print(f'- {t3} ', end=' ')
