time = list()
dados = dict()
index = num = 0

while True: 
    dados['nome'] = str(input('\nDigite o nome do jogador: ')) # => nome do jogador
    dados['gols'] = [] # => lista pra guardar os gols
    dados['totalJogos'] = int(input(f'\nQuantos jogos {dados["nome"]} jogou? ')) 

    for contGols in range(dados['totalJogos']): # => para cada jogo, pergunte quantos gols ele fez em cada um deles
        dados['gols'].append(int(input(f'\nQuantos gols fez no {contGols + 1}° jogo? '))) 
    time.append(dados.copy()) # => adiciona todos na lista 'time'

    resp = str(input('\nQuer continuar?[S/N] '))
    if resp not in 'Ss':
        print('\nPrograma encerrado!')
        break

print('='*55)
print()

print('-'*55)
print(f"{'N.°':<5}{'Nome':<12}{'Gols':<20}Total")
for pessoa in time:
    print('-'*55)
    print(f"{num:<5}{str(pessoa['nome']):<12}{str(pessoa['gols']):<20}{pessoa['totalJogos']}")
    num += 1
print('-'*55)

while index != 999:
    index = int(input("\nQual jogador deseja ver os dados? [999 para sair]\n> "))

    if index in range(0, len(time)):
        print(f"\nDados do jogador {time[index]['nome']}:\n")

        # Mostra os gols e em quais jogos   
        for j in range(0, len(time[index]["gols"])):
            print(f"""No jogo {j + 1} foram feitos {time[index]["gols"][j]} gols.""")
    
    else:
        print("Não existe um jogador com esse número, por favor tente novamente.")