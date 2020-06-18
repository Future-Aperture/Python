# mems aoisa do ex anterior mas invés de média é soma


contador = 0 
soma = 0
numeros = 0

while True:
    
    

    numeros = int(input('\nDigite um número inteiro[999 para parar]:\n> '))
    
    if numeros == 999: # parar programa
       break
    
    else: 
        soma += numeros 
        contador += 1    

   

print(f'O total de números digitados foi de {contador} e sua soma fica {soma}')