#  exercicio de media mais uma vez nesta jornada incrivel que é aprender python

ficha = {}


ficha['nome'] = str(input('\nDigite o nome do aluno: ')) 
ficha['media'] = float(input('\nDigite a média do aluno: '))

media = None

if ficha['media'] >= 7:
    media = 'Aprovado!'

elif ficha['media'] >= 5 and ficha['media'] < 7:
    media = 'Recuperação!'

else:
    media = 'REPROVADO!'

print('=-'*40)
print(f'''
    - Nome do aluno: {ficha['nome']}
    - Média do aluno: {ficha['media']:.2f}
    - Seu estado: {media}
    ''')
print('=-'*40)