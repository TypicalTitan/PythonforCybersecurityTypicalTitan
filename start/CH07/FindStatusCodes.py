#!/usr/bin/env python3
# Script that scans web server logs for status codes
# Use RegEx to find and report on most frequent status messages
# By TypicalTitan

# Import Python modules (re is Python's regular expression module)
import os
import re

# Prompt for file to analyze
log_file = input("Which file to analyze? ")

# Build the full path to the log file, starting from the folder this script is in
script_path = os.path.abspath(__file__)
script_dir = os.path.dirname(script_path)
file_path = os.path.join(script_dir, log_file)

# Open the file and load every line into a list
with open(file_path, "r") as f:
    log_lines = f.readlines()

# Regex pattern: a space, exactly 3 digits, then another space
# The parentheses "capture" the 3 digits so we can pull them out later
status_pattern = r'\s(\d{3})\s'

# Empty dictionary to count each status code, e.g. {"200": 5, "404": 2}
status_counts = {}

# Check every line for a status code
for line in log_lines:
    # re.search gives back a match if the pattern is found, or None if not
    match = re.search(status_pattern, line)
    if match:
        # group(1) is the text the parentheses captured: the 3-digit code
        code = match.group(1)
        # Add 1 to this code's count, or start it at 1 the first time we see it
        if code in status_counts:
            status_counts[code] += 1
        else:
            status_counts[code] = 1

# Sort the codes from least to most common, so the most common prints last
for code in sorted(status_counts, key=status_counts.get):
    print(code, status_counts[code])
