num1 = float(input("Digite o primeiro valor: "))
num2 = float(input("Digite o segundo valor: "))
num3 = float(input("Digite o terceiro valor: "))

numeros = [num1, num2, num3]
numeros.sort(reverse = False)

print(f"O menor valor é {numeros[0]} e o maior valor é {numeros[2]}")