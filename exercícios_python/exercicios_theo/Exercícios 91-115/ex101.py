# => programa para aprovar ou negar votos

    
    
def voteTester(): 
    from datetime import date
    
    # => cálculo idade
    ano = date.today().year
    idade = ano - nascimento

    if idade < 16:
        print(f'Com {idade} anos, voce NÃO vota!')
    
    elif idade >= 16 and idade < 18 or idade > 65:
        print(f'Com {idade}, seu voto é OPCIONAL!')
        
    else:
        print(f'Com {idade} anos, seu voto é OBRIGATÓRIO!')


    
nascimento = int(input('Ano de seu nascimento:\n> '))


voteTester()
