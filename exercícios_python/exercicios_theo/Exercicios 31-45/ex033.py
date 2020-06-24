#   maior e menor valor de 3 inputs


print('') # espaço inicial

#   perguntas
a = float(input('Primeiro valor: '))
b = float(input('Segundo valor: '))
c = float(input('Terceiro valor: '))


#   maior e menor(por enquanto)
menor = None
maior = None

#   maior
if a > b and a > c: 
    maior = a

elif b > a and b > c:
    maior = b

else:
    maior = c 

#   menor
if a < b and a < c:
    menor = a

elif b < a and b < c:
    menor = b

else:
    menor = c

print(f'''
Entre os 3 números...

E o menor é {menor:.2f}

O maior é {maior:.2f}
''')

