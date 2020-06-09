print('''\nCONVERSÃO DE TEMPERATURAS


Digite "C" para C°(Celsius) e "F" para F°(Fahrenheit).''')

while True:
    
    escolha = input(f"\nQual valor quer converter?\n")  

    if escolha.lower() == "c":
        C = float(input("\nDigite o valor de C°(Celsius): "))

        F = ((9 * C) / 5) + 32

        print(f"{C} C° é o mesmo que {round(F, 1)} F°.")
        break
    elif escolha.lower() == "f":
        F = float(input("\nDigite o valor de F°(Fahrenheit): "))

        C = (F - 32) * (5 / 9)

        print(f"{F} F° é o mesmo que {round(C, 1)} C°.")
        break
    else:
        print("Opção invalida. Tente novamente.\n")
        continue