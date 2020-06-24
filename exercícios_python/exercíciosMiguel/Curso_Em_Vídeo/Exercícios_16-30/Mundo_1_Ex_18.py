from math import cos, sin, tan, radians

angulo = float(input("Digite o valor do ângulo: "))
radiano = radians(angulo)

print(f"\nEm relação a o ângulo de {round(angulo, 1)}°, o valor aproximado do seno é {round(sin(radiano), 2)}, o cosseno {round(cos(radiano), 2)}, e a tangente {round(tan(radiano), 2)}")