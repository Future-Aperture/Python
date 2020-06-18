opcao = "S"
numeros = []

while opcao == "S":
    num = int(input("Digite um número inteiro para adiciona-lo a lista.\n> "))
    
    if not num in numeros:
        numeros.append(num)
    else:
        print("\nValor duplicado, não vou adicionar.\n")
        
    opcao = input("Deseja continuar? [S/N]\n> ").upper()

numeros.sort()

print(f"\nTodos os números digitados sem repetições são: {numeros}")