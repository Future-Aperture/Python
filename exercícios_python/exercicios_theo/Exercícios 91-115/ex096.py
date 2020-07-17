def area(altura, largura):
    area = altura * largura
    print(f'Com altura de {altura} e largura de {largura}, a área fica {area}m²')


a = float(input('Digite a altura: ')) 
l = float(input('Digite a largura: '))
area(a, l)
