""" Basic Relationship Utility part c

Ohm's law table of values, simple fixed loop
"""
import sys

print("Welcome\nThe Wee Ohm's Law Program!")
print("It asks for a resistance, \nIt displays a table of currents and voltages.")

resistance = float(input(
    "Please enter a resistance in ohms: "))
current_start = float(input(
    "Please enter a lower value for current in amps eg. 0.1: "))
current_stop = #* complete this, 
    #* asking for an upper value for current in amps
number_of_values = int(input(
    "Please say how many rows you want in the table "))

if number_of_values == 0:
    sys.exit("That can't work")

if current_stop < current_start:
    sys.exit("That can't work, sorry.")

step_size = (current_stop-current_start)/(number_of_values-1)
print("Current/A\tResistance/ohms\t\tVoltage/V")
print("---------\t---------------\t\t---------")

for i in range(0,number_of_values):
    #* work out the current for each step on this line
    #* work out the voltage for each step on this line
    print(round(current,2), '\t\t', resistance, '\t\t', round(voltage,2))


