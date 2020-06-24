#   media < 5 reprovado
#   media entre 5 e 6.9 recuperação
#   media > 7 aprovado
from time import sleep

print('')

print('Cálculo de média')
print('')
sleep(0.5)


#   notas
nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
print('')


#   media
media = (nota1 + nota2) / 2

if media >= 7:
    print('')
    print(f'Sua média ficou {media:.2f}, você está aprovado!')

elif media > 5 and media <= 6.9:
    print(f'Sua media ficou {media:.2f}, você está de recuperação.')
 
else:
    print(f'Sua media ficou {media:.2f}, você está reprovado!')