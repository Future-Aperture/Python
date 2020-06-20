palavras = ('palavra', 'luckhaos', 'Maicon Kuster', 'Lucas hype', 'Lorenzo ', 'biroliro', 'uniao', 'flasco',
'rexona', 'boiola', 'capope', 'poct poct', 'Favela', 'poesia', 'acustica', 'raffa', 'moreira')


for item in palavras:
    print(f'Na palavra {item}, suas vogais são', end=' ') 
    for letra in item: 

        if letra in 'aeiou':
            print(f'{letra}', end=' ')
    print()

  