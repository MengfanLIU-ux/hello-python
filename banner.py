import pyfiglet

name = input("What is your name? ")
print(pyfiglet.figlet_format(name))

color = input("What is your favorite color? ")
print(f"{color} is a nice color!")