#!/usr/bin/env python3
# Script that checks if a number is prime
# Prime numbers are greater than 1 and have no divisors other than 1 and itself
# By TypicalTitan

# Function that returns True if number is prime, otherwise False
def is_prime(number):
    # Primes must be greater than 1
    if number < 2:
        return False
    # Check every possible divisor from 2 to number - 1
    for x in range(2, number):
        if number % x == 0:
            return False
    # No divisors found
    return True

# Prompt the user for a number
number = int(input("Enter a number: "))

# Report the result
if is_prime(number):
    print("{0} is prime".format(number))
else:
    print("{0} is NOT prime".format(number))
