a = int(input("Digite a medida do primeiro lado: "))
b = int(input("Digite a medida do segundo lado: "))
c = int(input("Digite a medida do terceiro lado: "))

if a + b > c and a + c > b and b + c > a:
    print(f"\nAs medidas {a}, {b} e {c} podem SIM formam um triângulo.")

    if a == b and a == c:
        print("E esse triângulo é equilátero.")
    elif a == b or b == c or a == c:
        print("E esse triângulo é isósceles.")
    else:
        print("E esse triângulo é escaleno.")

else:
    print(f"\nAs medidas {a}, {b} e {c} NÃO formam um triângulo.")  