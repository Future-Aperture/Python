from random import randint

pc = player = vitorias = 0
parImpar = ""

while True:
    player = int(input("\nDigite um valor:\n> "))
    parImpar = input("Par ou Ímpar? (P/I)\n> ").lower()

    pc = randint(0, 10)

    print(f"\nVocê jogou o número {player} e o computador {pc}. O número {pc + player} é {'par' if (pc + player) % 2 == 0 else 'ímpar'}.\n")

    if parImpar == "p":
        if (pc + player) % 2 == 0:
            vitorias += 1
            print("Você VENCEU!!!\n\nVamos jogar novamente...")

        else:
            print(f"Você PERDEU!!!\nVocê conseguiu ganhar do computador {vitorias} vezes.")
            break

    elif parImpar == "i":
        if (pc + player) % 2 != 0:
            vitorias += 1
            print("Você VENCEU!!!\n\nVamos jogar novamente...")

        else:
            print(f"Você PERDEU!!!\nVocê conseguiu ganhar do computador {vitorias} vezes.")
            break

    else:
        print("Opção invalida.\n")