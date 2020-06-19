from random import randint

jokenpo = ("Pedra", "Papel", "Tesoura")

pc = randint(1, 3)

player = int(input('''
O que você quer jogar?

1. Pedra
2. Papel
3. Tesoura

> '''))

print("-+-" * 15)

derrota = bool((pc == 1 and player == 3) or (pc == 2 and player == 1) or (pc == 3 and player == 2))

vitoria = bool((player == 1 and pc == 3) or (player == 2 and pc == 1) or (player == 3 and pc == 2))

print(f'''\nVocê jogou {jokenpo[player - 1]}.
O computador jogou {jokenpo[pc - 1]}.''')

if derrota:
    print("\nVocê perdeu!")
elif vitoria:
    print("\nVocê ganhou!")
else:
    print("\nVocês empataram!")