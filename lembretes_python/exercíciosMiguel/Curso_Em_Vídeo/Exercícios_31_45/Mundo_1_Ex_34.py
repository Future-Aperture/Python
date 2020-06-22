salario = float(input("Quanto você ganha mensalmente? "))

if salario > 1250:
    salario *= 1.10
else:
    salario *= 1.15

print(f"Após o aumento do seu salario, agora você irá ganhar R$ {round(salario, 2):.2f} por mês.")