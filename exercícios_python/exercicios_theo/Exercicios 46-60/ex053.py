#   palíndro

frase = input('\nDigite a frase e veja se a frase é um palíndromo: ').replace(' ', '').upper()

inverso = ''

for c in reversed(frase):
    inverso += c
    
if inverso == frase:
    print('\nÉ um palíndromo')

else:
    print('\nNão é um palíndromo')

