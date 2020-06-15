print('')

r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Esses segmentos podem formar um triângulo!')

    if r1 == r2 and r2 == r3 and r1 == r3: #  equilatero
        print('Esse triângulo é classificado como EQUILÁTERO')
    
    elif r1 == r2 or r2 == r3 or r1 == r3: #   isoceles
        print('Esse triângulo é classificado como ISÓSCELES')
    
    else: # escaleno
        print('Esse triângulo é classificado como ESCALENO')


else: # não pode formar
    print('Esses segmentos NÃO podem formar um triângulo.')

