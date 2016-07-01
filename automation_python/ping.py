#!/usr/bin/python

from pprint import pprint
import os
import jtextfsm as textfsm


hostname = "192.168.1.254" #example
response = os.system("ping -c 6 " + hostname)

if response == 0:
      print hostname, 'is up!'
else:
    print hostname, 'is down!'

