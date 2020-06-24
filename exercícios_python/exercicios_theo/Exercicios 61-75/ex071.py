print('='*30)
print('Banco do Xesque')
print('='*30)

valor = int(input('\nQual a quantidade que você quer sacar?\n> '))

cedula = 50
totalCedula = 0

while True:
    if valor >= cedula:
        valor -= cedula
        totalCedula += 1

    else:
        if totalCedula > 0:
            print(f'Total de {totalCedula} cédulas de R${cedula}')
            if cedula == 50:
                cedula = 20
            elif cedula == 20:
                cedula = 10
            elif cedula == 10:
                cedula = 1
            totalCedula = 0
            if valor == 0:
                break   