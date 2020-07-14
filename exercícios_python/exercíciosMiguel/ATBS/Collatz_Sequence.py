def collatz(number):
    if number % 2 == 0:
        print(number // 2)
        return number // 2

    else:
        print(3 * number + 1)
        return 3 * number + 1


try: 
    num = int(input("Input a whole number bigger than 1:\n> "))

except ValueError:
    raise Exception("That's not a interger, please try again.")


if num < 1:
    raise Exception("Please, do NOT type a number less than 1.")

while num != 1:
    num = collatz(num)