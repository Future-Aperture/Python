#   quantidade de 'A's
#   posição do primeiro 'A'
#   posição do último 'A'
#   'rfind' lê o codigo de trás pra frente
#   '.count' Conta o total de strings


print('')

frase = str(input('Digite uma frase: ')).strip()

print(f'''

A letra 'A' apareceu {frase.lower().count('a')}

O primeiro 'A' apareceu na posição: {frase.lower().find('a')}

O último 'A' apareceu na posição: {frase.lower().rfind('a')}

''')

print('')
