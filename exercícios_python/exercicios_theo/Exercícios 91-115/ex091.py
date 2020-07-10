# programa que emula um dado
from random import randint
from time import sleep
from operator import itemgetter

ordem = [] # => lista com os números organizados

# => cálculos

print('-='*20)
jogos = {
    'jogador1':randint(1,7),
    'jogador2':randint(1,7),
    'jogador3':randint(1,7),
    'jogador4':randint(1,7)
}
rank = list()

# => mostra os resultados
for nome,num in jogos.items(): # => nome pega o 'ID'
    print(f'{nome} tirou {num}') # => num pega o valor gerado
    sleep(0.3)
    ordem.append(num)

rank = sorted(jogos.items(), key=itemgetter(1), reverse=True) # => retorna em rank, de maior pra menor
 
print('=-'*20)
sleep(0.5)

print()
print(f'{"RANKING:":>20}')
print()
print('-='*20)
for indice,valor in enumerate(rank):
   print(f'{indice + 1}° lugar foi: {valor[0]} que tirou {valor[1]} ')
print('-='*20)

# => valor[0] = nome do colocado (ordem decresente)
# => valor[1] = o valor que ele tirou no dado
# => 'indice' = mesma coisa que um contador
