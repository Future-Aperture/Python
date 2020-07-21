
dados = dict() # => dicionário geral
dadosGerais = list()
notas = list()

print('-'*20)
print('Dados escolares')
print('-'*20)    



while True:
    media = 0
    notas.clear() # => limpa a lista de notas
    dadosGerais.append(dados) # => adiciona o dicionário pra lista

    dados['nomeAluno'] = str(input('Nome do aluno: '))
    quantidadeDeNotas = int(input(f'Quantas notas deseja ver do aluno? '))

    # => for das notas
    for c in range(quantidadeDeNotas):
        notas.append(float(input(f'   - Digite a {c+1}° nota: '))) 
    dados['notasAluno'] = notas
    dados['media'] = sum(notas) / quantidadeDeNotas

    # => checa se quer continuar
    resp = str(input('Deseja continuar?[S/N]\n>'))
    if resp not in 'Ss':
        break
    elif resp != 's' and resp != 'n':
        print('Por favor digite apenas S ou N')

    else:
        continue

print(dadosGerais)

# => caro Theo do futuro, só falta fazer o output bonitinho
