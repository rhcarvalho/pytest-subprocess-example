import sys


def greet_100(name, age):
    try:
        age = int(age)
    except ValueError:
        raise ValueError("Sorry, I could not understand your age!")
    year = str((2014 - age)+100)
    return name + " will be 100 years old in the year " + year


def main():
    name = input("What is your name: ")
    age = input("How old are you: ")
    try:
        print(greet_100(name, age))
    except ValueError as exception:
        print(exception, file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
