#pessoas = {'nome': 'Theo', 'sexo': 'M', 'idade': '15'}
#for k,v in pessoas.items():  #  k => keys || v => values
    #print(f'{k:>7} = {v}')

# <============================================================>

#brasil = []

#estado1 = {'nome':'Rio de Janeiro', 'sigla':'RJ'}
#estado2 = {'nome':'São Paulo', 'sigla':'SP'}
#brasil.append(estado1)
#brasil.append(estado2)

#print(brasil[0]['nome']) # pegar o NOME do primeiro estado
#print()
#print(brasil[1]['sigla']) # pega a sigla do segundo estado

# <============================================================>

estados = dict()
brasil = list()

for c in range(0,3):
    estados['nome'] = str(input('\nNome do estado: '))
    estados['sigla'] = str(input('\nSigla do estado: '))
    brasil.append(estados.copy())

print(brasil[0]['nome'])