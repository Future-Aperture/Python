from random import randint
from operator import itemgetter

players = {}
posicao = 1

print("\nValores sorteados:")
for i in range(1, 5):
    players[f"Jogador {i}"] = randint(1, 6)

for j, k in players.items():
    print(f"{j} jogou o dado e tirou: {k}")

sortedPlayers = sorted(players.items(), key = itemgetter(1), reverse = True)

print("\nPosições de acordo com os valores sorteados:")

for l in sortedPlayers:
    print(f"    {l[0]} ficou em {posicao}° lugar com: {l[1]}")
    posicao += 1