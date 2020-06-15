print('')


#   inputs peso, altura e cálculo do IMC
peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))
imc = peso / altura ** 2
print('')


print(f'O seu IMC fica {imc:.2f}') #    mostra o valor do imc

#   estruturas
if imc <= 18.5:
    print('Você está abaixo do peso!')

elif imc <= 25:
    print('Você está no peso ideal.')

elif imc <= 30:
    print('Você está em sobrepeso!') 

elif imc <= 40:
    print('Você está obeso! Procure ajuda!')

elif imc >= 40:
    print('Você está em obesidade mórbida!!!!')