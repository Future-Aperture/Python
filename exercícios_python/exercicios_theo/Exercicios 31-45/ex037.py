#   binario, octal e hexadecimal
from time import sleep

print('')


numero = int(input('Digite um número inteiro qualquer: '))


#   opçoes
escolha = int(input('''
[ 1 ] Binário 
[ 2 ] Octal 
[ 3 ] Hexadecimal 

Escolha: '''))
#   fim das opçoes  
sleep(0.3)

if escolha == 1:
    print(f'O número {numero} convertido para binário fica {bin(numero)[2:]}') #    binario

elif escolha == 2: #    octal
    print(f'O número {numero} convertido para octal fica {oct(numero)[2:]}')

elif escolha == 3: #    hexadecimal
    print(f'O número {numero} convertido para hexadecimal fica {hex(numero)[2:]}')

else:
    print('Opção inválida. Tente novamente.')