#!/usr/bin/env python3
# Script that encrypts/decrypts text using cryptography module
# By TypicalTitan

# May need 'pip3 install cryptography' prior to running

# Import the Fernet (symmetric encryption) class
from cryptography.fernet import Fernet

# Create a new random key and return it as a string
def fernet_create_key():
    key = Fernet.generate_key()
    return key.decode()

# Encrypt plain_text with key, return cipher text as a string
def fernet_encrypt(plain_text, key):
    # Convert text and key to bytes
    b_plain = plain_text.encode()
    b_key = key.encode()
    # Encrypt data
    b_cipher = Fernet(b_key).encrypt(b_plain)
    # Convert back to string for display
    return b_cipher.decode()

# Decrypt cipher_text with key, return plain text as a string
def fernet_decrypt(cipher_text, key):
    # Convert text and key to bytes
    b_cipher = cipher_text.encode()
    b_key = key.encode()
    # Decrypt data
    b_plain = Fernet(b_key).decrypt(b_cipher)
    # Convert back to string for display
    return b_plain.decode()

# Prompt user for method
method = input("Encrypt, Decrypt, or Key (e/d/k) ").lower()[0]

# Call the appropriate function
if method == "e":
    message = input("Message: ")
    key = input("Key: ")
    print(fernet_encrypt(message, key))
elif method == "d":
    message = input("Cipher text: ")
    key = input("Key: ")
    print(fernet_decrypt(message, key))
elif method == "k":
    print(fernet_create_key())
else:
    print("Wrong selection, try again")
