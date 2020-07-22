# # # => def checa par ou impaor

# # def par(numero=0):
# #     if numero % 2 == 0:
# #         return numero
# #     else:
# #         return numero
    
    
    
# # numero = int(input('Digite um número:\n> '))

# # if par(numero):
# #     print(f'O número {par()} é par!')
    
# # else:
# #     print(f'O número {par()} é impar!')

# def numero(*numero):
#     return num
    
    
# num = int(input('Digite um número:\n> '))   
 
# print(numero())

# <=====================================================>

def fatorial(num):
    f = 1 
    for c in range(1, num+1):
        f *= c
    return f

num = int(input('Digite um valor:\n> '))
fat = fatorial(num)

print(f'O fatorial de {num} é {fat}')