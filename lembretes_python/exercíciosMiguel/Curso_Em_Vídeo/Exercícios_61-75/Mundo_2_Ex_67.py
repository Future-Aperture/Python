while True:
    num = float(input("\nInsira um valor para saber sua tabuada:\n> "))
    print("")

    if num < 0:
        print("Programa encerrado com sucesso.")
        break

    for g in range (1, 11):
        print(f"{num} X {g} = {num * g}")