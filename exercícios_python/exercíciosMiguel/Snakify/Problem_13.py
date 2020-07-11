# «Fractional part»

from math import modf

num = float(input("Type a fractional number:\n> "))

print(f"The decimal value of {num} is: {round(modf(num)[0], 5)}")