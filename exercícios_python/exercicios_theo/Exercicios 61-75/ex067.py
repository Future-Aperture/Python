
print('-'*30)
print('TABUADA VERSAO 3.0 MALUCO')
print('-'*30)

multiplo = int(input('Digite o número que deseja ver a tabuada:\n> '))


for numeros in range(1, 11):
    if multiplo < 0:
        break
    
    print(f'{numeros} X {multiplo} = {numeros * multiplo}')
    


    

print('\nTabuada encerrada! Tente novamente.')
