#   nome, sexo, idade de 4 pessoas
#   media de idade
#   homem mais velho
#   quantas mulheres tem menos de 20 anos
#   joga as idades para a lista com append e dps veja a maior idade


from time import sleep

media = 0
mulheres_anos = 0

for pessoas in range(1, 5):
    print(f'-----{pessoas}° PESSOA-----') #    numero da pessoa
    sleep(0.25)
    
    nome = input('Nome: ')
    idade = int(input('Idade: '))
    sexo = input('Sexo: ').lower().replace('Masculino', 'm')
    
    #   calculo media
    media += idade
media = media / 4  #    transforma 'media' em uma média de verdade  

mais_velho = [] # lista vazia pra ver qual a maior idade 


print(f'A média de idade do grupo é de {media:.2f}')
