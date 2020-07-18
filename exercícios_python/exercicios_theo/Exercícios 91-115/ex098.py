from time import sleep

def linha():
    print('--'*20)


def contador(inicio, fim, passo):
    if fim > inicio: # => normal
        for c in range(inicio, fim + 1, passo):
            print(c,end=' ')
            sleep(0.3)
    
    else: # => invertido
        for c in range(inicio, fim - 1, passo):
            print(c, end=' ')
            sleep(0.3)


linha()
contador(1, 10, 1) # => contagem de 1 => 10
print()

contador(10, 0, -2) # => contagem de 10 => 0 de 2 em 2

# <===================================>


print()

linha()
print('Agora personalize seu contador!')

inicio = int(input('Início: '))
fim = int(input('Final: '))
passo = int(input('Passo: '))

contador(inicio, fim + 1, passo)
linha()

print()