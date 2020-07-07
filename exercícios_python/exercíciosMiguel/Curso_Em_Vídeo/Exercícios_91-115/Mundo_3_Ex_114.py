import urllib.request

url = input("Digite a URL do site [Exemplo: https://www.google.com]:\n> ")

try:
    status = urllib.request.urlopen(url).getcode()
    if status:
        print(f"\nConsegui acessar o site '{url}' com sucesso.")

except urllib.error.URLError:
    print(f"\nNão foi possivel acessar o site '{url}' no momento." )