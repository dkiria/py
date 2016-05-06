#!/usr/bin/python
import time
import sched, time
import threading
import paramiko
import os
import sh
from sh import ifconfig
import re
#commands:   tr069.pl read wan test14 ip   , ifconfig eth2.241| perl -nle's/dr:(\S+)/print $1/e'



def do_something(sc):
    print "Doing stuff..."
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect('192.168.1.254',username='root',password='shitNobrod',timeout=1)
    stdin, stdout, stderr = ssh.exec_command("tr069.pl read wan test14 ip",timeout=1,
            get_pty=True)
    ip = stdout.read()
    print ip
    mdict=(
             "^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$",
       #     ".............................",
                );
    for value in mdict:
        m=re.match(value,'192.168.240.62')
        print m
        if m :
            print ('find match')
            ip=m.group()
            print ("ip is : " +ip)
            return ip

        else:
                print "error"
                sc.enter(6, 1, do_something, (sc,))


s = sched.scheduler(time.time, time.sleep)
s.enter(6, 1, do_something,(s,))
s.run()



