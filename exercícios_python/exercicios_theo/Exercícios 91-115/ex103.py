
def ficha(nome='<desconhecido>',gols=0):
    print(f'O jogador {nome} fez {gols} gol(s) ')


n = str(input('Digite o nome do jogador: '))
g = str(input(f'Quantos gols {n} fez? '))


if g.isnumeric():
    g = int(g)

else:
    g = 0

if n.strip() == '':
    ficha(gols=g)
else:
    ficha(n, g)

# ficha() <== não precisa pois eu já chamei no 'else'
