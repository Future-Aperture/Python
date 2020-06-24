numeros = [[], []]

for i in range(0, 7):
    num = int(input("Digite um número inteiro: "))

    if num % 2 == 0:
        numeros[0].append(num)
        
    else:
        numeros[1].append(num)

print(f'''
Os valores ímpares são: {sorted(numeros[1])}
os valores pares são: {sorted(numeros[0])}''')