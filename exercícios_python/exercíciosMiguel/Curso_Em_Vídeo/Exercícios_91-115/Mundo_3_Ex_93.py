ficha = {}

print("-=" * 15)
ficha["nome"] = input("Digite o nome do(a) jogador(a): ").title()
ficha["gols"] = []
ficha["total"] = 0

jogos = int(input("De quantos jogos ele participou: "))
print()

for i in range(1, jogos + 1):
    ficha["gols"].append(int(input(f"Quantos gols foram feitos no {i}° jogo: ")))
    ficha["total"] += ficha["gols"][i - 1]

print("-=" * 15)
print(ficha)
print("-=" * 15)

for j, k in ficha.items():
    print(f"No campo '{j}' tem o(s) valor(es): {k}")
print("-=" * 15)

for m, n in enumerate(ficha["gols"]):
    print(f"Na partida {m + 1}, fez {n} gols.")

print(f"Foi um total de {ficha['total']} gols.")