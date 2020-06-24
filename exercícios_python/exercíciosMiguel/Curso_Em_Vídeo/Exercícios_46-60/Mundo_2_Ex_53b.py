frase = input("Digite a uma frase:\n> ").strip()

fraseR = frase.replace(" ", "").lower()

invertida = ""

for j in reversed(fraseR):
    invertida += j

if invertida == fraseR:
    print(f'A frase "{frase}" é um palíndromo.')
else:
    print(f'A frase "{frase}" NÃO é um poaíndromo.')