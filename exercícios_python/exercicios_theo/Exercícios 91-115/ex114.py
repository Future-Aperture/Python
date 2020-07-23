
import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://pudim.com.br')

except urllib.request.URLError:
    print('\nNÃO consegui acessar o site pudim.com')

else:
    print('\nCONSEGUI com sucesso acessar o site pudim.com')


