#!/usr/bin/python3
import getpass
import sys
import telnetlib

HOST = "192.168.1.254"
user = "root"
password = getpass.getpass()

tn = telnetlib.Telnet(HOST)

tn.read_until("login: ")
tn.write(user + "\n")
if password:
    tn.read_until("Password: ")
    tn.write(password + "\n")
    tn.write("ls\n")
    tn.write("exit\n")
    print tn.read_all()
