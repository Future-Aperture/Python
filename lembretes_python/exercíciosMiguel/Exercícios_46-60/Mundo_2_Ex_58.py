from random import randint

rng = randint(0, 10)
count = 0
num = -1

while num != rng:
    num = int(input("\nAdivinhe o número de 0 à 10.\n> "))

    if num != rng:
        count += 1
        if num > rng:
            print("\nTente um pouco menos...")
        elif num < rng:
            print("\nTente um pouco mais...")

print(f"\nParabéns, você acertou!\nForam {count} tentativas até você conseguir adivinhar.")