num = int(input("Digite um número inteiro:\n> "))

for i in range(2, num // 2):
    if num % i == 0:
        print(f"\nO número {num} não é primo pois é divisivel por {i}.")
        break
    else:
        print(f"\nO número {num} é primo.")
        break