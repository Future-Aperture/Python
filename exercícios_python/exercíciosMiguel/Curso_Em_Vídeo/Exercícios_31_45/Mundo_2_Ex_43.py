print("-" * 15)
peso = float(input("Insira o seu peso em kg: "))
altura = float(input("Insira sua altura em centímetros: "))
print({"-" * 15})

imc = round(peso / altura * altura, 2)

print(f"\nVocê possui um IMC de {imc}, ou seja, você está:")

if imc < 18.5:
    print("abaixo do peso.")
elif imc >= 18.5 and imc < 25:
    print("com o peso ideal.")
elif imc >= 25 and imc < 30:
    print("acima do peso.")
elif imc >=30 and imc < 40:
    print("com obesidade.")
else:
    print("PARECENDO UM PLANETA KKKKKKKKKJJJJ!")