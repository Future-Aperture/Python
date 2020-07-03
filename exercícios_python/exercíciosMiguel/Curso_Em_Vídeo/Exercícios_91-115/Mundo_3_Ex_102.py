def fatorial(num, calc = False):
    """
    -> Calcula o fatorial de um número.
    :param num: O número usado para cacular o fatorial (int).
    :param calc: Mostrar o calculo feito para encontrar o fatorial (bool).
    :return: O resultado do fatorial (int)
    """
    fat = 1
    
    while num > 0:
        #Calcula o fatorial
        fat *= num
        
        #Caso queira ver a conta
        if calc:
            print(num, end = ' * ' if num > 1 else f" = {fat}")
        
        num -= 1

    return fat


#Inputs
num = int(input("Digite um número para saber seu fatorial:\n> "))
calculo = bool(int(input("Deseja ver a conta do calculo? [0 para NÃO]\n> ")))
print()

# Função
resultado = fatorial(num, calculo)

print(f"\nO resultado de !{num} é {resultado}")