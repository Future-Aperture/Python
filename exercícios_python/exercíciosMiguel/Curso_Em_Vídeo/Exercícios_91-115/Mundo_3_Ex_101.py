# Função para saber se vc pode votar
def voto(ano):
    from datetime import date
    
    #Calcula a idade
    idade = date.today().year - ano

    #Menor de idade
    if idade < 16:
        return f"Você não pode votar com {idade} anos.\n"
    
    # Maior de idade
    elif idade <= 18:
        return f"Você é obrigado a votar com {idade} anos.\n"

    # Pode se quiser
    else:
        return f"Você pode votar com {idade} anos.\n"


# Output e input do ano
anoInput = int(input("Digite seu ano de nascimento:\n> "))
print(voto(anoInput))