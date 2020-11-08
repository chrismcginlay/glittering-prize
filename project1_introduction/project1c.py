""" Basic Relationship Utility part c

Ohm's law table of values, simple fixed loop
"""
import sys

print("Welcome\nThe Wee Ohm's Law Program!")
print("It asks for a resistance, \nIt displays a table of currents and voltages.")

resistance = float(input(
    "Please enter a resistance in ohms: "))
current_start = input(
    "Please enter a lower value for current in amps eg. 0.1: ")
current_stop = input(
    "Please enter an upper value for current in amps eg. 1.0: ")
number_of_values = int(input(
    "Please say how many rows you want in the table "))

# if user doesn't type anything, set default values.
if current_start == '':
    current_start = 0.1
else:
    # have to use float separately now, so can check for empty string first
    current_start = float(current_start)

if current_stop == '':
    current_stop = 1.0
else:
    current_stop = float(current_stop)

if number_of_values == 0.0:
    sys.exit("That can't work")

if current_stop < current_start:
    sys.exit("That can't work, sorry.")

step_size = (current_stop-current_start)/(number_of_values-1)
print("Current/A\tResistance/ohms\t\tVoltage/V")
print("---------\t---------------\t\t---------")

for i in range(0,number_of_values):
    current = current_start + step_size*i
    voltage = current*resistance
    print(round(current,2), '\t'*2, resistance, '\t'*2, round(voltage,2))


