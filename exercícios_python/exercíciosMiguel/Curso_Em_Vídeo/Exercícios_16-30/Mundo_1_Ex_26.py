frase = input("Digite uma frase, para adquirir algumas curiosidades sobre ela.\n").lower().strip()

if frase.find("a") < frase.find("ã"):
    primeira = frase.find("a")
else:
    primeira = frase.find("ã")

if frase.rfind("a") > frase.rfind("ã"):
    ultima = frase.rfind("a")
else:
    ultima = frase.rfind("ã")

print(f'''A letra 'A' aparece {frase.count("a") + frase.count("ã")} vezes.
A letra 'A' aparece pela primeira vez na posição {primeira}, e pela ultima vez na posição {ultima}.''')