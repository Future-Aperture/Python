# O delay, pra ficar bunitu
from time import sleep

# Funcao que busca pelo maior número inserido
def maior(* num):
    print("\nAnalisando números...")

    # Output dos números
    for i in num:
        sleep(0.2)
        print(i, end = "; ")

    print(f"\nDos {len(num)} números digitados, o maior foi o {max(num)}.")


# Usa a função maior()
maior(6, 1, 3, 7, 8, 10, 3, 0)

print()
maior()

print()
maior(12, 64, 23, 982, 1, 0, 34)