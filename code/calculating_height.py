#!/usr/bin/env python3
"""
calculating_height.py
This program calculates a person's height in inches
"""

def main():
    print("I'm going to ask you to enter your height in two parts, feet and inches.")
    feet = eval(input("Enter your height in feet: "))
    inches = eval(input("Enter the rest of your height in inches: ")
    total_height_inches = feet * 12 + inches
    print("Your total height in inches is",total_height_inches)
    
    # Now we'll have them grow!
    total_height_inches = total_height_inches + 1
    print("You grew! Your height is now",total_height_inches)
    
main()

