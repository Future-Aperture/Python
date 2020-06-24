
print('--'*30)
print('BORA JOGAR PAR OU ÍMPAR RAPAZEADA KKKKKKKKKKMKKKKKKKKKMKKKKMKMMMKKMMMMJK')
print('--'*30)

from random import randint

vitorias = 0



while True:
    # numero aleatorio
    computador = randint(0, 10)

    # escolhas do player
    player = int(input('\nDigite um número inteiro:\n> '))
    escolha = str(input('PAR OU ÍMPAR[P/I]?\n> ')).strip().upper()
    
    # cadeia de ifs
    if escolha in 'Pp' and (player + computador) % 2 == 0: # loop que se quebra ate perder
        print(f'Parabéns, você ganhou, eu tirei {computador}')
        vitorias += 1

    elif escolha not in 'PIpi':
        print('É só par ou impar imbecil')
        print('Tente novamente.\n')

    else:
        print(f'''
Você perdeu.
Ganhou {vitorias}x consecutivas. ''')
        break

        
        
        