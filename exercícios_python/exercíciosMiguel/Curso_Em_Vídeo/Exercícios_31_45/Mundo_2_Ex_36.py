price = float(input("Digite o valor da casa: R$ "))
salary = float(input("Digite o seu salario mensal: R$ "))
year = int(input("Em quantos anos deseja pagar? "))

prestacao = round(price / (year * 12), 2)

if prestacao < salary / 0.3:
    print(f"\nO valor das prestações será de R$ {prestacao}. Não poderás pagar pela casa. Pois tu és pobre, pestista!")
else:
    print(f"\nO valor das prestações será de R$ {prestacao}. Você pode pagar pela casa! Seja feliz!")
