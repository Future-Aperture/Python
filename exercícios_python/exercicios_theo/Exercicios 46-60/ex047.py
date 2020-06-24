#   mostra numeros pares entre 1 e 50
#   end=' ' deixa na mesma linha

for numero in range(1, 51):
    if numero % 2 == 0:
        print(numero, end=' ' )