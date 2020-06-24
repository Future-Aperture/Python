print('')

from datetime import date
from time import sleep


ano = int(input('Que ano quer analisar? Digite 0 para analisar o ano atual: '))

if ano == 0:
    ano = date.today().year

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0: # calculo ano bissexto
    print('') # espaço
    print('Esse ano é bissexto!')
    sleep(0.25)

else:
    print('')    
    print('Esse ano não é bissexto!')



    