print('')


nome = str(input('Digite seu nome completo: '))



print(f'''

Nome: {nome}

Primeiro nome: {nome.split(' ')[0]}

Último nome: {nome.split(' ')[len(nome.split(' ')) - 1]}


''')