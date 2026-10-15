#!/usr/bin/env python3
# Sample script that writes to a file
# By Stepan Varganov, 10/13/2026
name=input("Enter your name: ")
color=input("Enter your favorite color: ")
pet=input("What is your pets name?: ")
mothers_maiden_name=input("What is your mothers maiden name?: ")
elementary_school=input("What elementary school did you attend?: ")
hackme=open("hackme.txt", "w")
hackme.write(f"Name: {name}\n")
hackme.write(f"Favorite Color: {color}\n") 
hackme.write(f"Pet's Name: {pet}\n")
hackme.write(f"Mother's Maiden Name: {mothers_maiden_name}\n")
hackme.write(f"Elementary School: {elementary_school}\n")
hackme.close()