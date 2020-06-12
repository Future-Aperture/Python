#   analisador de texto
#   quantidade 1° nome
#   quantidade de tudo

print('')

nome = input('Digite seu nome: ')
print('')

print(f'''
Nome : {nome}

Tudo maiúsculo: {nome.upper()}

Tudo minúsculo: {nome.lower()}

Letras ao todo: {len(nome.replace(' ', ''))}

Quantidade de letras do 1° nome: {len(nome.split(' ')[0])}

''')