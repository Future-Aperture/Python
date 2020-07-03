# O contador
def contador(i, f, p):
    num = i
    
    # Verifica se progressivo ou regressivo
    if i < f:
        while num <= f:
            print(num, end = " | ")
            num += p
    elif i > f:
        while num >= f:
            print(num, end = " | ")
            num += p
    print("Fim!")


# Contador de 1 à 10
print("Contador de 1 à 10, com passo 1\n")
contador(1, 10, 1)

# Contador de 10 à 0, passo 2
print("\nContador de 10 á 0, com passo 2\n")
contador(10, 0, -2)

# Contador customizado, pega as inputs
inicio = int(input("\nDigite o número inicial:\n> "))
fim = int(input("Digite o número final:\n> "))
passo = int(input("Digite o valor do passo:\n> "))

# Printa o contador customizado
print(f"\nContador de {inicio} à {fim}, com passo {passo}")
contador(inicio, fim, passo)