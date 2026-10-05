#!/usr/bin/env python3
# First example of pinging from Python
# By Stepan Varganov, 10/5/2025

import os

#Set IP Address
address = "192.168.1.1"

#Build Ping CMD
ping_cmd = f"ping -c 1 -w 1 {address}"

#Run Ping
status_code = os.system(ping_cmd)

#print(f"Ping status code: {status_code}")
if status_code == 0:
    print(f"{address} is reachable")
else:
    print(f"{address} is not reachable")