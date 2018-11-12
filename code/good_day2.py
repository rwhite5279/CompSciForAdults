#!/usr/bin/env python3
"""
good_day2.py
Write a program that has the user enter the time in 24-hour format, 
where 1200 = noon and 2400 = midnight. The program should then print
out a 'Good morning!', "Good afternoon!", or 'Good evening!'
message depending on the time of day.
"""

def main():
    time = eval(input('Enter the time of day (in 24-hour format): '))
    if time < 1200:
        print("Good morning!")
    elif time < 1800:
        print("Good afternoon!")
    else:
        print("Good evening!")

main()


