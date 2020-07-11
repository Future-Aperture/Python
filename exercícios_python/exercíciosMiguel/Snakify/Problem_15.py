# <<Digital clock>>

pastMidnight = int(input("How many minutes went past midnight?\n> "))

hour = pastMidnight // 60 
minute = pastMidnight % 60

print(f"\nThat's the same as: {hour}:{minute}a.m.")