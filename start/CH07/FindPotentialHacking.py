#!/usr/bin/env python3
# Script that scans web server logs for possible hacking
# Use RegEx to find and report on common hacking types
# Based on https://www.cgisecurity.com/fingerprinting-port80-attacks-a-look-into-web-server-and-web-application-attack-signatures-part-two.html
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

# Every pattern below is built from the same two halves, with the suspicious
# character(s) in the middle, so we only search inside the requested URL
#   request_start: the opening quote, the method (GET, POST...) and a space
#   request_end:   the rest of the URL, then " HTTP/1.1" and the closing quote
request_start = r'"\w+ ([^"]*'
request_end = r'[^"]*) HTTP\/\d\.\d"'

# * is a wildcard in shell commands, like "ls *"
wildcard_pattern = request_start + r'\*' + request_end
# Backticks run commands in shell and Perl
backtick_pattern = request_start + r'`' + request_end
# Characters common in program code but rare in normal URLs: ^ [ ] # { } "
code_pattern = request_start + r'[\^\[\]#{}\"]' + request_end
# Parentheses, as in a JavaScript call like alert(1)
# (CSS here means cross-site scripting, the older name for XSS)
css_pattern = request_start + r'[\(\)]' + request_end
# Two or more dots in a row, as in ../ which climbs out of the website's folder
folder_traversal_pattern = request_start + r'\.{2,}' + request_end

# Check every line against every pattern
# These are separate ifs (not elif), so one line can be flagged more than once
for line in log_lines:
    if re.search(wildcard_pattern, line):
        print("Possible attack: Wildcard in URI")
        print(f"\t{line.strip()}")
    if re.search(backtick_pattern, line):
        print("Possible attack: Backtick (`) in URI")
        print(f"\t{line.strip()}")
    if re.search(code_pattern, line):
        print("Possible attack: Code in URI")
        print(f"\t{line.strip()}")
    if re.search(css_pattern, line):
        print("Possible attack: Potential CSS in URI")
        print(f"\t{line.strip()}")
    if re.search(folder_traversal_pattern, line):
        print("Possible attack: Folder Traversal in URI")
        print(f"\t{line.strip()}")
