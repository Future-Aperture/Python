# Verifica se o input são apenas números
def leiaDinheiro(msg):
    while True:
        money = input(msg).strip().replace(",", ".")
        if not money.isalpha():
            return float(money)

        else:
            print("\nPor favor, digite apenas números. Tente novamente.")
            continue