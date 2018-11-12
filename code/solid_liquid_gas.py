#!/usr/bin/env python3
"""
solid_liquid_gas.py
This program asks the user to enter the current temperature, in degrees 
Fahrenheit. The program should then print out state of H2O at that temperature: 
"solid", "liquid", or "gas".
"""

def main():
    water_temp_F = eval(input("What's the temperature of the H20 (degrees F)? "))
    if water_temp_F < 32:
        print("This H20 is frozen SOLID")
    elif water_temp_F < 212:
        print("This H20 is LIQUID")
    else:
        print("This H20 is a steaming hot GAS")

main()

