#!/usr/bin/env python3
# Sample script that reads from a file
# By Stepan Varganov, 10/14/2026
with open("hackme.txt", "r") as hackme:
    print("Here is someone to hack - information:")
    print(hackme.read())
