#!/usr/bin/env python3
"""
random_walker1.py
This program models a "random walker" that starts at location 0,0, an 
intersection in the middle of a city laid out in square blocks. Each turn, 
the random walker moves one block to the north, east, west, or south, with
the x-coordinate changing by 1 block or the y-coordinate changing by one
block.

Print out the move number and the location of the random walker after every
turn. How long does it take the random walker to return home?
"""

import random

def main():
    x = 0
    y = 0
    turns = 0
    print("The random walker is starting at position", x, y)
    while not(x == 0 and y == 0) or turns == 0:
        randint = random.randrange(4)
        if randint == 0: x = x + 1
        elif randint == 1: y = y + 1
        elif randint == 2: x = x - 1
        else: y = y - 1
        turns = turns + 1
        print(turns, x, y)
    print("We're back!")
    

main()

