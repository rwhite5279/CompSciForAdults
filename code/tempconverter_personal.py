#!/usr/bin/env python3

"""
tempconverter_personal.py
Converts temperature in Fahrenheit to temperature in Celsius
"""

def main():
    name = input("Enter your name: ")
    degreesF = eval(input("Enter the temperature in degrees Fahrenheit: "))
    degreesC = (5 / 9) * (degreesF - 32)
    print(name, ", the equivalent temperature is", degreesC, "degrees Celsius.")

main()