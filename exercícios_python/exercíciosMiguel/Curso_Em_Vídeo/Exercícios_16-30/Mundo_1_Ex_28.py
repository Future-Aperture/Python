from random import randint

rng = randint(0, 5)

while True:
    num = int(input("Adivinhe o número de 0 à 5.\n"))
    
    if num == rng:
        print("\nParabéns, você acertou!")
        break
    else:
        print("\nTente novamente")