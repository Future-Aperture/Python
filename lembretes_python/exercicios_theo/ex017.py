from math import hypot 
from time import sleep

print('')


ct = float(input('Digite o valor do cateto oposto: ')) #    cateto oposto
print('')


cd = float(input('Digite o valor do cateto adjacente: '))
print('')
sleep(0.35)

print(f'O valor da hipotenusa fica {hypot(ct, cd):.2f}')

