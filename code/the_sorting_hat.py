#!/usr/bin/env python3
"""
the_sorting_hat.py
This program uses a random number generator to simulate the
Sorting Hat from the Harry Potter stories.
"""

import random

def main():
    randint = random.randrange(4)   # gets 0-3 randomly
    if randint == 0:
        print("Gryffindor!")
    elif randint == 1:
        print("Hufflepuff!")
    elif randint == 2:
        print("Ravenclaw!")
    else:
        print("Slytherin!")

main()

