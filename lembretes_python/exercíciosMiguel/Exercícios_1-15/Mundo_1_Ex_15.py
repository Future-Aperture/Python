km = float(input("Digite a quilometragem percorrida com o carro: "))

dias = int(input("Quantos dias você ficou com o carro?"))

valorTotal = (dias * 60) + (km * 0.15)

print(f"\nO valor que você terá que pagar pelo alguel do carro é: R$ {round(valorTotal, 2):.2f}")