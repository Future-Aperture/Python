from time import sleep

# => listas e dicionários
pessoas = dict()
galera = list()

# => càlculos
soma = media = 0
quantidadeMulheres = 0 # => contador da quantidade de mulheres
acimaMedia = 0 # => contador de pessaos acima da media

while True:    
    pessoas.clear()
    pessoas['nome'] = str(input('\nDigite seu nome:\n> ')).title()
    pessoas['idade'] = int(input('\nDigite sua idade:\n> '))
    soma += pessoas['idade']
    pessoas['sexo'] = str(input('\nDigite seu sexo[M/F]:\n> ')).upper()
    
    while pessoas['sexo'] not in 'MmFf':
        print('\nPor favor digite somente M ou F. Imbecil')
        pessoas['sexo'] = str(input('\nDigite seu sexo[M/F]:\n> ')).upper()
    galera.append(pessoas.copy())
       
    resp = str(input('\nDeseja continuar? [S/N]: '))
    if resp in 'Nn': # => caso digite nao
        print('\nObrigado!')
        print('Encerrando sistema...')
        sleep(0.5)
        print('Encerrado!')
        break # => pra nao voltar pro inicio]

print('-='*40)
print(f'Total de pessoas cadastradas: {len(galera)}') # => total de pessoas

media = soma / len(galera) # => cálculo das somas
print(f'Média de idade: {media:.0f} anos.') # => média de idade

print(f'Listas de mulheres cadastradas:',end=' ')
# se o sexo da pessoa analisada foi mulher:
for p in galera:
    if p['sexo'] == 'F': 
        print(p["nome"],end=' ')
        
# => se a pessoa está acima da média de idade
print('\nLista de pessoas acima da média de idade: ',end=' ')
for p in galera:
    if p['idade'] >= media:
        print(p["nome"],end=' ')
print(f'\n{"-="*40}')
