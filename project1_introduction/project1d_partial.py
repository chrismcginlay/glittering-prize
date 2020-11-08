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
    #* add two lines for voltage
    #* just like for resistance section above
#* write an if here to check the length of the current string
    #* add two lines for current
    #* again just like for resistance section above

if not (GOT_R or GOT_V or GOT_I):
    sys.exit("You gave me nothing. I can't help you. Goodbye")

if not ((GOT_R and GOT_V) or (GOT_R and GOT_I) or (#* last combo? ):
    sys.exit("You only gave me one thing. I need two things, sorry.")

if GOT_R and GOT_I and GOT_V:
    v_check = current*resistance
    #* if statement to check that v_check == what voltage user typed here
        print("Success, your values are consistent")
    else:
        print("Your values are not consistent")
        print("My result is V = ", v_check, ", not ", voltage)
    
elif not GOT_R: # let's calculate R
    resistance = voltage/current
    print("The resistance is ", resistance, " ohms")
    
#* on these three lines you should do another
    #* elif for situation that we don't got V. Calculate V and
    #* print it nicely just like above elif for resistance.

else: # has to be I then.
    try:
        current = voltage/resistance
        print("The current is ", current, " amps")
    except ZeroDivisionError:
        print("Current would be infinite if resistance is zero.")

print("Program finished.")


