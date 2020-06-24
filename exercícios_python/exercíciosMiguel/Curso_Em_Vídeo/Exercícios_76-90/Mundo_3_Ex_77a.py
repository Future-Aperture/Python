palavras = ("Cana-De-Açucar", "Ana", "Banana", "Chupou", "Destruidor", "Palavra", "Theo")
vogais = ("a", "i", "u", "e", "o")

for i in range(0, len(palavras)):

    print(f"\nNa palavra {palavras[i].upper()} temos as vogais: ", end = "")
    
    for j in vogais:
        if j in palavras[i].lower():
            print(j, end = " ")