#!/usr/bin/python
import os
import subprocess
import ConfigParser
import sys
import os
from ConfigParser import SafeConfigParser
from fabric.api import abort, cd, env, get, hide, hosts, local, prompt, \
    put, require, roles, run, runs_once, settings, show, sudo, warn
from fabric.contrib.console import confirm
from getpass import getpass
from ConfigParser import SafeConfigParser

#ef parser():
parser = SafeConfigParser()
config_file = raw_input("configfile: ") # doesnt matter if we echo username so use raw_input()
parser.read(config_file)


for section_name in parser.sections():
	print 'Section:', section_name
#        print '  Options:', parser.options(section_name)
	env.hosts =parser.get(section_name, 'ip')
        print env.hosts



print "start"
subprocess.call("./html_parser.sh")
print "end"
lis = list()
for line in open('parser.txt'):
	if line != '\n':
		ldir = line.rstrip('\n')
		
		print" \n" +  ldir
		lis.append(ldir)
#		for line in lis:
#			print lis
#print line
#print lis[1]
