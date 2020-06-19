palavras = ("Cana-De-Açúcar", "Ana", "Banana", "Chupou", "Destruidor", "Palavra", "Théo")

for i in palavras:
    print(f"\nNa palavra {i.upper()} temos as vogais: ", end = "")

    for j in i.lower():
        if j in "aáàãâíiuúeéêíoô":
            print(j, end = " ")