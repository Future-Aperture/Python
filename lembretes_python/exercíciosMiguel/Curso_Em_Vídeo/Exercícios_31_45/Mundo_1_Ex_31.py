viajem = int(input("Digite a distancia, em Km, da sua viajem: "))

if viajem <= 200:
    print(f"\nO valor da sua viajem vai ser: R$ {viajem * 0.5:.2f}")
else:
    print(f"\nO valor da sua viajem vai ser: R$ {viajem * 0.45:.2f}")