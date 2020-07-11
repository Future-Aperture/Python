# <<Car route>>
from math import ceil


km = int(input("Type de km per day the car travels:\n> "))
distance = int(input("Type the distance the car has to travel:\n> "))

print(ceil(distance / km))