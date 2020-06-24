# «School desks»

std1 = int(input("Input the first ammount od students: "))
std2 = int(input("Input the second ammount od students: "))
std3 = int(input("Input the third ammount od students: "))

desks = (std1 // 2) + (std2 // 2) + (std3 // 2) + (std1 % 2) + (std2 % 2) + (std3 % 2)

print(f"\nIn total, we'll need {desks} desks")