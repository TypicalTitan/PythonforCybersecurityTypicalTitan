#!/usr/bin/env python3
# Script that scans web server logs for client addresses
# Use RegEx to find and report on most frequent users
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

# Regex pattern: everything at the very start of the line (^) up to the first space
# \S+ means "one or more characters that aren't spaces"
# The client is usually an IP address, but sometimes the server logs a
# hostname instead (like ...googleusercontent.com), so we don't require digits
client_pattern = r'^(\S+)\s'

# Empty dictionary to count how many requests each client made
client_counts = {}

# Check every line for the client's address
for line in log_lines:
    match = re.search(client_pattern, line)
    if match:
        # group(1) is the address the parentheses captured
        client = match.group(1)
        # Add 1 to this client's count, or start it at 1 the first time we see it
        if client in client_counts:
            client_counts[client] += 1
        else:
            client_counts[client] = 1

# Sort from fewest to most requests, so the busiest client prints last
for client in sorted(client_counts, key=client_counts.get):
    print(client, client_counts[client])
