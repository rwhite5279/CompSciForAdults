#!/usr/bin/env python3
"""
secret_message.py
Write a program that has the user enter their name. The program
should then say "Hello, name", and then goodbye, to anyone who
enters their name. If it's *your* name, however, in addition to
hello and goodbye, the program should print out a 2-line 
message only for you.
"""

def main():
    name = input("Enter your name: ")
    print("Hello, ", name, "!")
    if name == "Richard":
        print("I have a secret message for you:")
        print("You're awesome!")
    print("Goodbye!")

main()


