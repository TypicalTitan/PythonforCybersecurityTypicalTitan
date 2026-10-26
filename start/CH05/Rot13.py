#!/usr/bin/env python3
# Script that encrypts/decrypts text using ROT13
# By TypicalTitan

# Function that rotates every letter in the message by 13 places
# Running it twice returns the original message (13 + 13 = 26 letters)
def rot13(source_message):
    # Convert message to lower-case for simplicity
    source_message = source_message.lower()
    final_message = ""

    # Loop through each letter in the source message
    for letter in source_message:
        # Convert the letter to its ASCII number
        ascii_num = ord(letter)
        # Only shift alphabetic (a-z = 97-122) characters
        if ascii_num >= 97 and ascii_num <= 122:
            # Add 13 to "shift" the letter
            new_ascii = ascii_num + 13
            # If we went past 'z', wrap around to the start of the alphabet
            if new_ascii > 122:
                new_ascii = new_ascii - 26
            # Convert the number back into a letter
            final_message = final_message + chr(new_ascii)
        else:
            # Spaces, numbers, and punctuation are kept as-is
            final_message = final_message + letter
    return final_message

# Prompt for the source message
message = input("What is the message to encrypt/decrypt? ")

# Print converted message
print("Message has been converted:")
print(rot13(message))
