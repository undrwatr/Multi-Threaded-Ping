#!/usr/bin/python

# Handle the imports needed for the program
import sys
import os
import platform
import subprocess
import threading

#Check for the type of platform that we will use
plat = platform.system()
scriptDir = sys.path[0]
hosts = os.path.join(scriptDir, 'hosts.txt')
hostsFile = open(hosts, "r")
lines = hostsFile.readlines()

#Based on the platfrom go through the hosts.txt file and then ping each host and output the data.
def ping(ip):
    if plat == "Windows":
        ping = subprocess.Popen(
            ["ping", "-n", "1", "-l", "1", "-w", "100", ip],
            stdout = subprocess.PIPE,
            stderr = subprocess.PIPE
        )

    if plat == "Linux":
        ping = subprocess.Popen(
            ["ping", "-c", "1", "-l", "1", "-s", "1", "-W", "1", ip],
            stdout = subprocess.PIPE,
            stderr = subprocess.PIPE
        )
    if plat == "Darwin":
        ping = subprocess.Popen(
            #["ping", "-c", "1", "-l", "1", "-s", "1", "-W", "1", ip],
            ["ping", "-c", "1", "-s", "1", "-W", "1", ip],
            stdout = subprocess.PIPE,
            stderr = subprocess.PIPE
        )

    out, error = ping.communicate()
    print out
    print error

for ip in lines:
    threading.Thread(target=ping, args=(ip,)).run()
