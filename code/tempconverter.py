#!/usr/bin/env python3

"""
tempconverter.py
Converts temperature in Fahrenheit to temperature in Celsius
"""

def main():
    degreesF = 50
    degreesC = (5 / 9) * (degreesF - 32)
    print(degreesF,"degrees F is equal to",degreesC,"degrees Celsius.")

main()