#!/usr/bin/env python3
"""
good_day1.py
Write a program that has the user enter the time in 24-hour format, 
where 1200 = noon and 2400 = midnight. The program should then print
out a 'Good morning!' greeting if it's before noon, and a 'Good day!'
message if it's noon or after.
"""

def main():
    time = eval(input('Enter the time of day (in 24-hour format): '))
    if time < 1200:
        print("Good morning!")
    else:
        print("Good day!")

main()


