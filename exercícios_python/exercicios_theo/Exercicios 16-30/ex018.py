from time import sleep
from math import cos, sin, tan


print('')
print('Seno, cosseno, tangente')
print('')
sleep(0.35)

#   var angulo
angulo = float(input('Digite o ângulo que deseja: '))

print (f'''

Seno: {sin(angulo):.2f}

Cosseno: {cos(angulo):.2f}

Tangente: {tan(angulo):.2f} ''')