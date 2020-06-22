from math import hypot

c1 = float(input("\nInsira o valor do cateto oposto: "))
c2 = float(input("Insira o valor do cateto adjacente: "))

print(f"\nO valor da hipotenusa dos catetos {c1} e {c2} é: {hypot(c1, c2)}")