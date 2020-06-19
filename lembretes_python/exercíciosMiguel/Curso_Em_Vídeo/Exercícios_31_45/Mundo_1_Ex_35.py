a = int(input("Digite a medida do primeiro lado: "))
b = int(input("Digite a medida do segundo lado: "))
c = int(input("Digite a medida do terceiro lado: "))

if a + b > c and a + c > b and b + c > a:
    print(f"\nAs medidas {a}, {b} e {c} podem SIM formam um triângulo.")  
else:
    print(f"\nAs medidas {a}, {b} e {c} NÃO formam um triângulo.")  