dados = {}

dados['nome'] = str(input('\nDigite o nome do jogador: ')) # => nome do jogador

dados['totalJogos'] = int(input(f'\nQuantos jogos {dados["nome"]} jogou? ')) # => totalJogos pega quantos jogos o cara jogou

for contGols in range(dados['totalJogos']): # => para cada jogo, pergunte quantos gols ele fez em cada um deles
    dados['gols'] = int(input(f'\nQuantos gols fez no {contGols + 1}° jogo? '))


# => Primeira forma: jeito primata de ser
print()      
print('-='*40)
print('Primeira forma:\n ')
print(dados)
print()

# => Segunda forma: fase da idade média de ser
print('-='*40)
print('Segunda forma:')
print()
for nome,valor in dados.items():
    print(f'O campo {nome} tem valor {valor}')
print()
print('-='*40)

# => Terceira forma: jeito humano evoluído de ser

print('Terceira forma:')
print(f'O jogador {dados["nome"]}:')

for key in range(dados["totalJogos"]):
    print(f'- No {key+1}° jogo, {dados["nome"]} fez {contGols} gols.')
print(dados)
    