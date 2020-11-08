""" Basic Relationship Utility part b

Introduce keyboard input. Sticking with Ohm's law
"""

print("Welcome\nThe Wee Ohm's Law Program!")
print("It asks, \n\tIt calculates, \n\t\tIt tells you how it is")

resistance = float(input("Please enter a resistance in ohms: "))
current = float(input("Please enter a current in amps: "))

voltage = resistance * current

print("V = \t", voltage, "\t volts")
