numeros = ("zero", "um", "dois", "três", "quatro", "cinco", "seis", "sete", "oito", "nove", "dez", "onze", "doze", "treze", "quatorze/catorze", "quinze", "dezesseis", "dezessete", "dezoito", "dezenove", "vinte")

while True:

    num = int(input("Digite um número de 0 à 20:\n> "))

    if num not in range(0,21):
        print("\nPor favor, tente novamente.\n")

    else:
        print(f"""
A forma por extenso do número {num} é: {numeros[num]}""")
        break