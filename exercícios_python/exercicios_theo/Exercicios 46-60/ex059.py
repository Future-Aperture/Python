# menu de opçoes
# 1 = somar // 2 = multiplicar // 3 = maior entre os dois
# 4 = novos numeros // 5 = exit


import math
from time import sleep


valor1 = float(input('\nDigite o primeiro valor: '))
sleep(0.25)
valor2 = float(input('Digite o segundo valor: ')) 


#   opçoes do menu(300 blocos de ifs)

while True:
    menu = int(input('''
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
    [ 1 ] somar

    [ 2 ] multiplicar

    [ 3 ] comparar

    [ 4 ] novos numeros

    [ 5 ] sair
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-  
> '''))  
    
    print('-='*14)

    # somar valores
    if menu == 1:
        print(f'Os dois valores somados ficam {valor1 + valor2}')
        break

    # multiplicar valores
    elif menu == 2:
        print(f'Os dois números multiplicados ficam {valor1 * valor2}')
        break

    # comparar valores 
    elif menu == 3:
        if valor1 > valor2:
            print(f'O maior valor entre os dois é {valor1}')
        elif valor2 > valor1:
            print(f'O maior valor entre os dois é {valor2}')
        elif valor1 == valor2:
            print('Os dois valores são iguais.')
            break

    # novos numeros        
    elif menu == 4:
        valor1 = float(input('\nDigite o primeiro valor: '))
        sleep(0.25)
        valor2 = float(input('Digite o segundo valor: '))
    
    else:
        break 
    
    print('-='*14)