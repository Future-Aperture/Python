frase = input("Digite a uma frase:\n> ").strip()

fraseR = frase.replace(" ", "").lower()

print("")

print(list(reversed(fraseR)))

if list(fraseR) == list(reversed(fraseR)):
    print(f'A frase "{frase}" é um palíndromo.')
else:
    print(f'A frase "{frase}" NÃO é um palíndromo.')