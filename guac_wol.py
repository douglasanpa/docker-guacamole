#!/usr/bin/env python2
#
# --------------------------Readme---------------------------------------
#
# Guacamole wake-on-lan (WOL) script. Luke P 26 Feb 2018
#
# This is designed to run on the Guac host machine and will send a
# 'magic-packet'wakeup call to a specified machine on the same
# network when a Guac connection attempt is made.
#
# Relies on Guac continually attempting a connect as most machines
# will not start up immediately (ie, there is no delay function from
# when the wakeup is sent to when Guac attempts a connect). Some
# machines may go through a full reconnect cycle before they fully
# wake up and a connection is established.
#
# Script reads a 'macs.list' file in the same directory as it runs from.
# File must contain only the header detail, and comma-separated fields
# of id (Guac connection number) and MAC addr. There is no error
# checking and it will likely fail if there are any other random
# characters in the file. Data from this file is compared to the
# ongoing connection data in /var/logs/tomcat7/catalina.out
# You would probably need to change this path if your system
# uses tomcat8.
#
# --- example macs.list --- #
# id,mac
# 1,11:22:33:44:55:66
# 2,22:33:44:55:66:77
# 3,33:44:55:66:77:88
# 4,44:55:66:77:88:99
# 5,55:66:77:88:99:00
# 6,66:77:88:99:00:aa
# etc,etc
# ----------------------------- #
#
# This is a rough 'n ready script and has not been tested for any length
# of time, nor on anything other than Guacamole 0.9.14 and Python 2.7 in
# Ubuntu 16.04. It is offered as a concept only, if you choose to try it
# and it works for you that's great, if it doesn't, or it somehow breaks
# your system I'd be sorry but please be aware I assume no responsibility
# or liability!
#
# -----------------------------------------------------------------------

import subprocess, csv, sys, socket

# Define a function to send magic packet to wakeup machine.
# Takes MAC address as input & will broadcast on default NIC

def WOL(mac):
    data = ''.join(['FF' * 6, mac.replace(':', '') * 16])
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    sock.sendto(data.decode("hex"), ("255.255.255.255",9))

# Open and tail Tomcat logfile. We can expect Guac connection
# data to be logged here. This includes the Guac username that connects
# out to another machine on the network, and the connection number from
# the connection list in Guac. This list appears to be numbered as the
# first being #2 (assume #1 is the logged in user that created the
# connection?).

logfile =
subprocess.Popen(['tail','-F','/var/log/tomcat7/catalina.out'],stdout=subprocess.PIPE,stderr=subprocess.PIPE)

# Start reading the logile data line by line as it arrives.
# Open the macs.list file to get machine connection numbers and associated
# MAC addresses. Then continue to read logfile for Guac username and
# connection number. If a match is found between the logged connection
# number & id number from list file, call the WOL function to wakeup the
# machine via the associated MAC address (ad infinitum).
#
# Could also use the username instead of id number but some users may
# have multiple connections....

while True:
    line = logfile.stdout.readline()
    with open('macs.list') as inifile:
        reader = csv.DictReader(inifile)
        if 'connected to connection' in line:
            q1 = line.find("\"")
            q2 = line.find("\"",q1+1)
            q3 = line.find("\"",q2+1)
            q4 = line.find("\"",q3+1)
            user = line[q1+1:q2]
            conn_num = line[q3+1:q4]
            for row in reader:
                if(row['id']) == conn_num:
                    WOL(row['mac'])
