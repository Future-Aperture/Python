times = ("Palmeiras", "Santos", "Vasco da Gama", "Grêmio", "Flamengo", "Corinthians", "Internacional", "Cruzeiro",
        "São Paulo", "Atlético Mineiro", "Botafogo", "Fluminense", "Coritiba", "Bahia", "Goiás", "Guarani",
        "Sport", "Portuguesa", "Atlético Paranaense", "Vitória")




# coritiba está em 13° pq n tem Chapecoense pq eles sao ruins dale

print(f'''
\nOs 5 primeiros colocados é {times[:5]}
Os últimos 4 colocados são {list(reversed(times[-4:]))}\n
Os times em ordem alfabética são {sorted(times)}
\nO Coritiba está na posição de {times.index('Coritiba') + 1 }° ''')

