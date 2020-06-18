print('')
print('--'*30)
print('CADASTRO DE PESSOAS')
print('--'*30)

# pessoas maiores de 18, quantos homens tem e mulheres com menos de 20 anos
maior18 = 0
homens = 0
mulheres = 0

while True:
    
    # cadastro
    idade= str(input('\nDigite sua idade:\n> '))
    sexo = str(input('Sexo[M/F]:\n> '))
    resposta = str(input('Deseja continuar[S/N]?\n> ')).strip().lower()

    if resposta in 'Ss':
        idade = str(input('\nDigite sua idade:\n> '))
        sexo = str(input('Sexo[M/F]:\n> '))
        resposta = str(input('Deseja continuar[S/N]?\n> ')).strip().lower()

    else:
        print('Saindo...')
        break

    if idade > 18: # pessoas com mais de 18 anos
        maior18 += 1

    elif sexo in 'Mm': # homens existentes
        homens += 1

    elif sexo in 'Ff' and idade < 20: # mulheres com menos de 20
        mulheres += 1


   


