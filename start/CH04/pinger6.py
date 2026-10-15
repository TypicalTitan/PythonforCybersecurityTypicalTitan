#!/usr/bin/env python3
# Sixth example of pinging from Python
# Writing log messages to a file
# By 
def is_divisible(num, div):
    if num % div == 0:
        return True
    else:
        return False
number = input("Enter a number: ")
divisor = input("Enter a divisor: ")
print("Is " + str(number) + " divisible by " + str(divisor) + "? " + str(is_divisible(int(number), int(divisor))))