# boletim com tuplas

fichaAlunos = list()


while True:
    nome = str(input('\nNome do aluno: ')) # nome da pessoa
    nota1 = float(input('Nota 1: ')) # 1° nota
    nota2 = float(input('Nota 2: ')) # 2° nota
    media = (nota1 + nota2) / 2 # calcula a média de cada aluno


    fichaAlunos.append([nome, [nota1, nota2], media]) # adiciona pra lista
    
    resposta = str(input('Deseja continuar? [S/N] '))
    if resposta in 'Nn': # se a resposta for NAO
        break
 
print('='*60)

# variavel => i = numero do aluno 

print(f'{"No.":<4} {"Nome":<10} {"Média":<8}')
print()
for i, a in enumerate(fichaAlunos):
    print(f'{i:<4} {a[0]:<10} {media:.2f}')
