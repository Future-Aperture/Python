from time import sleep

pessoas = dict()
galera = list()
while True:
    pessoas['nome'] = str(input('\nDigite seu nome:\n> ')).title()
    pessoas['idade'] = int(input('\nDigite sua idade:\n> '))
    pessoas['sexo'] = str(input('\nDigite seu sexo[M/F]:\n> '))
    galera.append(pessoas.copy())
    while pessoas['sexo'] not in 'MmFf':
        print('\nPor favor digite somente M ou F. Imbecil')
        pessoas['sexo'] = str(input('\nDigite seu sexo[M/F]:\n> '))
    

    resp = str(input('Deseja continuar? [S/N]: '))
    if resp in 'Nn':
        print('\nObrigado!')
        print('Encerrando sistema...')
        sleep(0.5)
        print('Encerrado!')
        break # => pra nao voltar pro inicio

# => calculo idade
for mediaIdade in (0, len(pessoas)):
    print(mediaIdade)



# => print de tudo
print(f'''
Total de pessoas cadastradas: {len(galera)}
 ''')

