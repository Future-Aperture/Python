from lxml import html
from googlesearch import search
import requests
import re


# <---------------------||-------------------->

listaPreco = [] # Preços
sites = [] # Sites que serão usados
precoAdquirido = [] # lxml.etree - arquivos que contém o preço
regex = re.compile(r"(\d\d|\d\d\d|\d.\d\d\d|\d\d.\d\d\d),\d\d") # Filtro dos preços

# <---------------------||-------------------->

busca = input("Digite o que você quer buscar:\n> ")

links = search(busca, num = 10, start = 0, stop = 10, pause = 2)

for j in links:
    if 'www.kabum.com.br' in j:
        sites.append(j)

# <---------------------||-------------------->

for k in sites.copy():
    page = requests.get(k)
    tree = html.fromstring(page.content)

    precoAdquirido = tree.xpath("//div[@class = 'preco_normal']/text()")

    if not precoAdquirido:
        precoAdquirido = tree.xpath("//div[@class = 'preco_antigo-cm']/text()")

    preco = ''.join(precoAdquirido)

    if preco and precoAdquirido:
        preco = regex.search(preco).group()
        listaPreco.append(preco)

    else:
        sites.remove(k)


# <---------------------||-------------------->

print(listaPreco)
print(f"Sites usados: {sites}")