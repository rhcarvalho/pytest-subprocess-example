def greet_100(name, age):
    try:
        age = int(age)
    except ValueError:
        raise ValueError("Sorry, I could not understand your age!")
    year = str((2014 - age)+100)
    return name + " will be 100 years old in the year " + year
