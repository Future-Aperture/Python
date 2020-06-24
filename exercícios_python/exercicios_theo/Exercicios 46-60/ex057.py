# programa que leia sexo masculino e f


while True:
    sexo = str(input('\nDigite seu sexo [M/F]: ')).strip().upper()
    if sexo in 'FM':
        print(f'\nSexo {sexo} regitrado com sucesso!')
        break
    else:
        print('\nPor favor tente novamente.')
