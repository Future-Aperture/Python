from random import randint

numeros = (randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100))

print("Todos os números da tupla são: ", end = "")
for i in numeros:
    print(i, end = " ")

print(f'''

O maior número da tupla é: {max(numeros)}
O menor número da tupla é: {min(numeros)}''')