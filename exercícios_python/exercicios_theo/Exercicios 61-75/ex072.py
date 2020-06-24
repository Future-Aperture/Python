extensos = 'zero', 'um', 'dois', 'tres','quatro', 'cinco', 'seis', 'sete', 'oito','nove','dez',
'onze', 'doze', 'treze', 'quatorze','quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte'


while True:
    numero = int(input('Digite um número de 0 a 20:\n> '))

    if numero < 0 or numero > 20:
        print('Tente novamente.\n')
    
    else: 
        print(f'O número {numero} em extenso fica {extensos[numero]}\n')
        break
    
    