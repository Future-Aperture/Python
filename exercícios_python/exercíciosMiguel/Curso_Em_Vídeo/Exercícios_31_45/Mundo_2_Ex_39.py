from datetime import date

year = int(input("Fala meu bom, em que ano você nasceu?  "))

ano = date.today().year
idade = ano - year

print(f"\nQuem nasceu em {year} tem {idade} em {ano}")

if idade < 18:
    print(f'''\nAinda faltam {18 - idade} anos para você poder se alistar.
Espere até o ano de {ano + (18 - idade)} para se alistar meu jovem.''')

elif idade > 18:
    print(f'''\nVocê está atrasado, seu alistamento era pra ter sido em {ano - (18 - idade)}.
Esse é um atrado de {idade - 18}, acho melhor correr caralho.''')

else:
    print(f"\nVocê tem 18 anos, agora já pode se alistar.\nE vá rápido filho de mil putas.")