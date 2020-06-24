

par = [ ]
impar = [ ]
numeros = [ ] # lista 2D geral

for perguntas in range(1, 8):
    numero = int(input('\nDigite um número: '))
    
    if numero % 2 == 0: # numeros pares
        par.append(numero)
    
    elif numero % 2 == 1: # numeros impares
        impar.append(numero)


numeros.append(par)
numeros.append(impar)

print('-='*40)
print(f'''
Os valores pares digitados foram {numeros[0]}
Os valores ímpares digitados foram {numeros[1]}

''')