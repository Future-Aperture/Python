
#   contador de quantos numeros foram digitados
contador = 0


numero = int(input('\nDigite um número inteiro[999 PARA PARAR]:\n> '))

while numero != 999:
    numero = int(input('Digite um número inteiro[999 PARA PARAR]:\n> '))
    contador += 1

print(f'O total de números digitados foi de {contador} número(s).')

