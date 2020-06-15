#   ver se é primo ou nao


numero = int(input('\nDigite um número: '))#  leitor do numero

#   numero primo
for i in range(2, numero // 2):
    
    if numero % i == 0:
        print(f'O número {numero} é primo.')
        break
    
    else:
        print(f'O número {numero} não é primo.')
        break