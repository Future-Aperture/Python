print(f'\n{"-" * 20}\n')

nota1 = float(input("Digite o valor da primeira nota: "))
nota2 = float(input("Digite o valor da segunda nota: "))

media = round((nota1 + nota2) / 2, 1)

print(f'\n{"-" * 20}')

if media < 5:
    print(f"\nVocê teve uma média de {media}, então foi REPROVADO!")

elif media >= 7:
    print(f"\nVocê teve uma média de {media}, então foi APROVADO!")

else:
    print(f"\nVocê teve uma média de {media}, então está de RECUPERAÇÃO!")

