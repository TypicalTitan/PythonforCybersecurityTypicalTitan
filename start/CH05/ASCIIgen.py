#!/usr/bin/env python3
# ASCII generator
# Uses chr() to create ASCII characters
# By TypicalTitan

# Print every ASCII number (0-126) next to the character it represents
for i in range(127):
    print("{0}\t'{1}'".format(i, chr(i)))

# Show the round trip: letter -> number -> letter
letter = "a"
number = ord(letter)
print("ord('{0}') = {1}".format(letter, number))
print("chr({0}) = '{1}'".format(number, chr(number)))
