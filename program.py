import sys


name = input("What is your name: ")
try:
    age = int(input("How old are you: "))
except ValueError:
    print("Sorry, I could not understand your age!", file=sys.stderr)
    sys.exit(1)
year = str((2014 - age)+100)
print(name + " will be 100 years old in the year " + year)
