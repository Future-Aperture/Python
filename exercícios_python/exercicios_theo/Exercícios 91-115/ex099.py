
allNum = []    


def maior(*num): # => função que printa o maior numero dentre a lista
    print(f'De {len(num)} números, o maior digitado foi {max(num)}')
                        
# => parte funcional do programa      
while True:
    numeros = int(input('Digite um número inteiro:\n> '))
    resp = str(input('Deseja continuar?[S/N]:\n> '))
    allNum.append(numeros)
    
    if resp in 'Nn':
        break

    
maior(allNum)
