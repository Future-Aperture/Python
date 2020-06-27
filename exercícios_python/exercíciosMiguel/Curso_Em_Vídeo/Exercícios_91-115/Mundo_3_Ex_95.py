# Declara as variaveis
ficha = {}
jogadores = []
opcao = "s"
index = num = 0

while opcao != "n":
    print("-=" * 15)
    
    # Input do nome e quantos jogos
    ficha["nome"] = input("Digite o nome do(a) jogador(a): ").title()
    ficha["gols"] = []
    ficha["total"] = 0

    jogos = int(input("De quantos jogos ele participou: "))
    print()

    # Quantos gols foram feitos por jogo
    for i in range(1, jogos + 1):
        ficha["gols"].append(int(input(f"Quantos gols foram feitos no {i}° jogo: ")))
        ficha["total"] += ficha["gols"][i - 1]

    #Adiciona a ficha para uma lista
    jogadores.append(ficha.copy())
    ficha.clear()

    opcao = input("\nVocê deseja continuar? [S/N]\n> ").lower()

print("-=" * 15)

# Deixa o output bonitinho
print(f"\n{'N.°':<5}{'Nome':<12}{'Gols':<20}Total")

for pessoa in jogadores:
    print(f"{num:<5}{str(pessoa['nome']):<12}{str(pessoa['gols']):<20}{pessoa['total']}")
    num += 1

# Usado para ver dados individuais
while index != 999:
    index = int(input("\nQual jogador deseja ver os dados? [999 para sair]\n> "))

    if index in range(0, len(jogadores)):
        print(f"\nDados do jogador {jogadores[index]['nome']}:\n")

        # Mostra os gols e em quais jogos   
        for j in range(0, len(jogadores[index]["gols"])):
            print(f"""No jogo {j + 1} foram feitos {jogadores[index]["gols"][j]} gols.""")
    
    else:
        print("Não existe um jogador com esse número, por favor tente novamente.")