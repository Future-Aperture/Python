times = ("Palmeiras", "Santos", "Vasco da Gama", "Grêmio", "Flamengo", "Corinthians", "Internacional", "Cruzeiro",
        "São Paulo", "Atlético Mineiro", "Botafogo", "Fluminense", "Coritiba", "Bahia", "Goiás", "Guarani",
        "Sport", "Portuguesa", "Atlético Paranaense", "Vitória")

print(f"""\nLista de todos os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol (2012):\n{times}

Os 5 primeiros times:\n{times[:6]}

Os últimos 4 times:\n{times[-4:]}

Em ordem alfabética:\n{sorted(times)}

O time do Fluminense está em {times.index('Fluminense') + 1}° colocado. """)