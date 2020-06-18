lista = []
pos = 0

for i in range(0, 5):
    num = int(input("Digite um número:\n> "))

    if i == 0 or num > lista[-1]:
        lista.append(num)

    else:
        while pos < 5:
            if num < lista[pos] or num == lista[pos]:
                lista.insert(pos, num)
                break
            
            pos += 1
                
print(f"\nA lista em ordem crescente fica: {lista}")