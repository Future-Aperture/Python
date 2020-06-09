#   celsius para fahrenheit
import time


print('')
print('CONVERSOR DE MEDIDAS')
time.sleep(1.0)
print('')


print('')
print('Digite (C) para °C e (F) para °F.')
time.sleep(0.6)
print('')


#   sistema das escolhas e escolhas
while True:
    escolha = str(input('Sua escolha: '))
    print('')
    time.sleep(0.5)

    if escolha.lower() == 'c':
        # celsius para fahrenheit
        
        c = int(input('Quantos graus Celsius deseja converter? °'))
        f = ((9 * c) / 5) + 32
        print('')
        time.sleep(0.5)
        print(f'O valor convertido para Fahrenheit fica °{round(f, 2)}')
        break

    elif escolha.lower() == 'f':
        # fahrenheit para celsius
        
        f = int(input('Quantos graus Fahrenheit deseja converter? °'))
        c = (f - 32) * (5 / 9)
        print('')
        time.sleep(1.0)
        print(f'O valor convertido para Celsius fica °{round(c, 2)}.')
        
        break

    else:
        time.sleep(0.2)
        print('ERROR! Tente novamente.')
        print('')
        continue

