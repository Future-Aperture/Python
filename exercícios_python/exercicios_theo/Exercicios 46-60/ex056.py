'''nome, sexo, idade de 4 pessoas
   media de idade
   homem mais velho
   quantas mulheres tem menos de 20 anos
   joga as idades para a lista com append e dps veja a maior idade
   jogar todos os nomes dos homens em uma lista '''


from time import sleep

# variaveis
mais_velho = [ ] # lista vazia pra ver qual a maior idade 
media = 0
mulheres_anos = 0 
nome_mais_velho = [ ]

# for principal
for pessoas in range(1, 5):
    print(f'-----{pessoas}° PESSOA-----') # numero da pessoa
    sleep(0.20)
    
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    sexo = str(input('Sexo: ').lower().replace('Masculino', 'm', )).replace('Feminino', 'f')
    
    if sexo == 'm':
        mais_velho.append(idade) # joga todas as idades do homens no mais_velho
        nome_mais_velho.append(nome)

    if sexo == 'f' and idade < 20:
        mulheres_anos += 1



    media += idade # calculo media de idade
media = media / 4  #    transforma 'media' em uma média de verdade  

posicao_mais_velho = mais_velho.index(max(mais_velho))
    

print(f'''

A média de idade do grupo é de {media:.2f}
O total de mulheres com menos de 20 anos é {mulheres_anos}
O nome do homem mais velho é {nome_mais_velho[posicao_mais_velho]}
E sua idade é {max(mais_velho)} ''') 

#   vapo