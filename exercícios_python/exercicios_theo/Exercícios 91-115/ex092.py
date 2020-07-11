from time import sleep
from datetime import datetime

print()
print('-='*40)
print(f'{"INFORMAÇÕES":^80}')
print('-='*40)
sleep(0.5)

pessoa = {}


pessoa['nome'] = str(input('\nDigite se nome:\n> ')) # => pega o nome da pessoa
sleep(0.2)

pessoa['idade'] = int(input('\nDigite sua data de nascimento: ')) # => pega a data de nacscimento
pessoa['idade'] = datetime.now().year - pessoa['idade'] # => calcula a idade da pessoa
sleep(0.2)

pessoa['carteiraTrabalho'] = int(input('Carteira de trabalho[0 não tem]: ')) # => vê se tem carteira de trablaho

if pessoa['carteiraTrabalho'] != 0: # => mostra informações adicionais || caso tenha carteiraTrabalho
    pessoa['anoContratacao'] = int(input('Ano de contratação: '))
    pessoa['salario'] = float(input('Seu salário: '))
    pessoa['aposentadoria'] = pessoa['idade'] + (35 - (datetime.now().year - pessoa["anoContratacao"]))
    
    print()
    print('-='*40)

for k,v in pessoa.items():
    print(f'{k}: {v}')

# 'Jão' foi especial na resolução deste exercicio.
# serviu de exemplo literalmente todas as vezes q testei o código