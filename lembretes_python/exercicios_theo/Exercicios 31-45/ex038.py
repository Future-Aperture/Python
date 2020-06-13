#   comparação de numeros

#   estilo inicial
print('')
print('Comparção de números inteiros')
print('')


#   variaveis de numeros
numero1 = int(input('Digite o primeiro valor: '))
numero2 = int(input('Digite o segundo valor: '))

print('')

if numero1 > numero2: # numero 1 maior
    print('O primeiro número é maior!')

elif numero2 > numero1: #   numero 2 maior
    print('O segundo número é maior!')

else:
    print('Os números são iguais!')
