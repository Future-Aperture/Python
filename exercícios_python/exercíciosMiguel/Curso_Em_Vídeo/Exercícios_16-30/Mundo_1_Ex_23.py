from random import randint

num = str(randint(0, 9999))
print(f"O número gerado foi: {num}")

print("\nOs números separados são: ")
for i in range(0, len(num)):
    print(num[i])