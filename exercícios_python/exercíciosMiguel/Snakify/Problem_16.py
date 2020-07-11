# «Total cost»
from math import modf

dolars = int(input("How many dolars one cupcake costs?\n>"))
cents = int(input("And how many cents?\n> "))
cents /= 100

num = int(input("How many cupcakes you want to buy?\n> "))

result = modf(num * (dolars + cents))

print(int(result[1]), result[0])