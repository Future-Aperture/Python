#   refazer ex061 pq tao sem criatividade 

print('-='*20)
print('Contador de uma P.A ')
print('-='*20 )

primeiroTermo = int(input('\nDigite o primeiro termo:\n> '))
razao = int(input('Digite a razão:\n> '))

contador = 1
limite = 11

while contador != limite:
    print(f'{primeiroTermo}', end=' ')
    contador += 1 
    primeiroTermo += razao

    if contador == limite:
        limite += int(input('\nDigite quantos valores deseja mostrar a mais. Digite 0 para encerrar. '))
        
print('ACABOU MEU CONFRADE')        