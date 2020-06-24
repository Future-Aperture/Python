#   jokenpo
from time import sleep
from random import randint

#   menu
print('')
print('-='*20)
print('JO-KEN-PO')
print('-='*20)
print('')

computador = randint(1, 3) # jogada do computador

lista = ['pedra', 'papel', 'tesoura']


player = int(input('''
O que você quer jogar?

[ 1 ] PEDRA
[ 2 ] PAPEL
[ 3 ] TESOURA

> '''))
#   empate
if player == computador:
    print('EMPATE!')


#   computador ganha
elif computador == 1 and player == 3 or computador == 2 and player == 1 or computador == 3 and player == 2:
    print(f'Eu ganhei de você, humano desprezível, eu joguei {lista[computador]}')

#   player ganha
else:
    print(f'Parabéns, você ganhou! Voce tirou {lista[player]}')
    print('')
    print('N̡̨̕͘͜Ã̸̡̧́͜Ơ͏͘͢,̴̴̛͝ ̴̡͢͡N͜͠Ã̶̛O̕͠,͘͢͞͠͞ ͘͠͡E̵̢͜U̶̷͡͏́ ̡Ǹ͠Á̵̀͟O̴͜ ̡̕͞͝P̢̛Ò̀̕͞͏S͘͘͡͝S͏̸̴̀͜O̶̷̢̨ ̷́Ṕ̵͠E͏̸̵͝R̷҉͢D̷̀̀́͘È̷Ŕ̷͡,͡͏̕͘͞ ̶̷҉̧É̴͟҉̶Ù̵͞ ̸̶̨͜͝V̷̛̛͠͞Ǫ͡͏L͠͠͝͞T҉̷͢͠A̶͢͞͠R̀́E̸I̴͟ ̵͞Ȩ̴́́M̷̢̀͘ ̡̕̕͟͡B͝͏̢̛̀R̷̛E̸͘͜V̵̨̨̛͠E̴͏͢͡,͘͝͡ ͞E͜͞҉ ̛̕͞M̴̛̀͝A͢͜͏̛́I̴̕͜͞Ś̴͜ ͏҉F͏̨͢͡͞Ò͏̸́Ŗ̷́͡T͠͝͏Ȩ̷ ')