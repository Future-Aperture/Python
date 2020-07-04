def ficha(nomeJ = "<desconhecido>", qGols = 0):
    print(f"O jogador {nomeJ} fez {qGols} gol(s) no campeonato.")


# Inputs de nome e gols
nome = input("Insira o nome do jogador:\n> ")
gols = input("Insira o número de gols feitos por ele:\n> ")
print()

# Se gols é um número
if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0

# Se tem um nome
if not bool(nome):
    ficha(qGols = gols)
else:
    ficha(nome, gols)