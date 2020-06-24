# «Two timestamps»

h1 = int(input("Type de first hours: "))
m1 = int(input("Type de first minutes: "))
s1 = int(input("Type de first seconds: "))

ts1 = (h1 * 60 * 60) + (m1 * 60) + s1

h2 = int(input("\nType de second hours: "))
m2 = int(input("Type de second minutes: "))
s2 = int(input("Type de second seconds: "))

ts2 = (h2 * 60 * 60) + (m2 * 60) + s2

print(f"\nThe diference in seconds between {h1}:{m1}:{s1} and {h2}:{m2}:{s2} is: {ts2 - ts1}")