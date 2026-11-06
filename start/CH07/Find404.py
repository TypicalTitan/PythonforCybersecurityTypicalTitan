#!/usr/bin/env python3
# Script that scans web server logs for 404 errors
# By TypicalTitan

import os

# Prompt for file to analyze
log_file = input("Which file to analyze? ")

# Build the full path to the log file, starting from the folder this script is in
# That way it finds the log no matter which folder you run the script from
script_path = os.path.abspath(__file__)
script_dir = os.path.dirname(script_path)
file_path = os.path.join(script_dir, log_file)

# Open the file for reading
f = open(file_path, "r")

# Read the file one line at a time, so only one line is in memory at once
while True:
    line = f.readline()
    # readline() gives back an empty string once it reaches the end of the file
    if not line:
        break
    # Print any line with "404" in it (404 is the "Not Found" status code)
    # Note: this matches 404 anywhere in the line, not just the status code
    if "404" in line:
        # strip() removes the newline at the end so the output isn't double-spaced
        print(line.strip())

# Close the file when we're done with it
f.close()
