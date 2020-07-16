from lxml import html
from googlesearch import search
import requests
import re


# <----------------------------------------->

listaPreco = [] # Preços
sites = [] # Sites que serão usados
precoNormal = [] # lxml.etree - arquivos que contém o preço
regex = re.compile(r"(\d\d|\d\d\d|\d.\d\d\d|\d\d.\d\d\d),\d\d") # Filtro dos preços

# <----------------------------------------->

busca = input("Digite o que você quer buscar:\n> ")

links = search(busca, num = 10, start = 0, stop = 10, pause = 2)

for j in links:
    if 'kabum' in j:
        sites.append(j)

# <----------------------------------------->

for k in sites:
    page = requests.get(k)
    tree = html.fromstring(page.content)


    precoNormal += tree.xpath("//div[@class = 'preco_normal']/text()")
    precoNormal += tree.xpath("//div[@class = 'preco_antigo-cm']/text()")

# <----------------------------------------->

for i in precoNormal:
    print(type(i))
    listaPreco.append(regex.search(str(i)).group())

# <----------------------------------------->

print(listaPreco)
print(f"Sites usados: {sites}")