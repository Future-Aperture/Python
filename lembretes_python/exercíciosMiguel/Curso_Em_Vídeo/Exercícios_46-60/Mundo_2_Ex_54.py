from datetime import date

ano = []
idade = []
qSim = 0
qNao = 0

for i in range (1, 8):
    ano.append(int(input(f"Digite o ano de nascimento da pessoa número {i}:\n> ")))
    print("")
    idade.append(date.today().year - ano[i - 1])

    if idade[i - 1] > 17:
        qSim += 1
    else:
        qNao += 1

print(f"\nDas 7 pessoas, {qSim} poderão participar e {qNao} não.")