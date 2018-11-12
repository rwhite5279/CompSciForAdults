#!/usr/bin/env python3

"""
personal_helloworld.py
This program accepts input from the user and prints out a
personalized message.
"""

def main():
    print("What's your name? ", end='')
    name = input()
    print("Hello, " + name + "!")


# Now we just need to call the main function to run it!
main()

