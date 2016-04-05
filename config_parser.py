#!/usr/bin/python
import sys
import ConfigParser
import getpass
import getopt
import glob
import pipes
import pexpect
import paramiko
import os
import re
import socket
from contextlib import closing
from ConfigParser import SafeConfigParser
from random import randint
from paramiko import SSHClient

Config = ConfigParser.ConfigParser()
config_file = raw_input("configfile: ") # doesnt matter if we echo username so use raw_input()
Config.read(config_file)
Config.sections()

def get_cfg_value(configfile, category, what, strict = 'yes'):
    ret = None
    parser = SafeConfigParser()
    # FIXME make the path configurable
    parser.read(configfile)

    try:
        ret = parser.get(category, what)
    except ConfigParser.NoSectionError:
        print('No section [%s] found in config file. Fix your config file' % category)
        if strict == 'yes':
            exit(1);
    except ConfigParser.NoOptionError:
        print('No option %s= found in config file. Fix your config file' % what)
        if strict == 'yes':
            exit(1);

    return ret

def ConfigSectionMap(section):
    	dict1 = {}
    	options = Config.options(section)
    	for option in options:
        	try:
			dict1[option] = Config.get(section, option)

			if dict1[option] == -1:
                		DebugPrint("skip: %s" % option)
        	except:
			print("exception on %s!" % option)
            		dict1[option] = None
	return dict1

for i in Config.sections():
	Name = ConfigSectionMap(i)#['file_Path']
	print "\n" +   i
	for value in Name:
		print value + ' = ' + Name[value]


for i in Config.sections():
	IP = ConfigSectionMap(i)['ip']
	USERNAME = ConfigSectionMap(i)['username']
	PASSWORD = ConfigSectionMap(i)['pass']
	FILEPATH = ConfigSectionMap(i)['file_path']
	SERVERPATH = ConfigSectionMap(i)['server_path']
	FILE = None
	try:
	    FILE = ConfigSectionMap(i)['file1']
	except:
		print "no file"
	list1 = list()
	if FILE != None:
		list1.append( FILE );
	print list1

	print "------------------------------" + "\n" + " " +  IP + USERNAME
