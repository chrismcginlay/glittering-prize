""" Basic Relationship Utility part d

Ohm's law. Determining correct course of action
The user will enter some of V, I, and/or R and we will act accordingly
"""
import sys

GOT_R = False
GOT_V = False
GOT_I = False

print("Welcome\nThe Wee Ohm's Law Program!")
print("You enter what you know. I work out the rest.")

resistance =input("Please enter a resistance in ohms or leave blank : ")
current = input("Please enter a current in amps or leave blank: ")
voltage = input("Please enter a voltage in volts or leave blank: ")

if len(resistance)>0:
    GOT_R = True
    resistance = float(resistance)  # turn into a decimal
if len(voltage)>0:
    GOT_V = True
    voltage = float(voltage)
if len(current)>0:
    GOT_I = True
    current = float(current)

if not (GOT_R or GOT_V or GOT_I):
    print("You gave me nothing. I can't help you. Goodbye")
    sys.exit()

if not ((GOT_R and GOT_V) or (GOT_R and GOT_I) or (GOT_I and GOT_V)):
    print("You only gave me one thing. I need two things, sorry.")
    sys.exit()

if GOT_R and GOT_I and GOT_V:
    v_check = current*resistance
    if v_check == voltage:
        print("Success, your values are consistent")
    else:
        print("Your values are not consistent")
        print("My result is V = ", v_check, ", not ", voltage)
    
elif not GOT_R: # let's calculate R
    resistance = voltage/current
    print("The resistance is ", resistance, " ohms")
    
elif not GOT_V: # let's calculate V
    voltage = current*resistance
    print("The voltage is ", voltage, " volts")

else: # has to be I then.
    try:
        current = voltage/resistance
        print("The current is ", current, " amps")
    except ZeroDivisionError:
        print("Current would be infinite if resistance is zero.")

print("Program finished.")


