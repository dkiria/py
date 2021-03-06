#!/usr/bin/python
import getopt
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
import sys
import sys
import subprocess
import time
from contextlib import closing
from ConfigParser import SafeConfigParser
from random import randint
from paramiko import SSHClient
#from scp import SCPClient

Config = ConfigParser.ConfigParser()
config_file = raw_input("configfile: ") # doesnt matter if we echo username so use raw_input()
Config.read(config_file)
Config.sections()

def scp (file_Path,server_Path, ip, username, password):
	os.system("scp "+file_Path + " " +USERNAME + "@" + IP + ":" + server_Path)

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

def ssh(ip,username,password):
	ssh = paramiko.SSHClient()
	ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	print "Input Your Credentials (password will not be echoed)"
	try:
        	ssh.connect(ip, 22, username, password)
        except paramiko.SSHException:
        	print "Connection Failed"
		quit()
        except socket.error:
        	print "Connection Failed"
		quit()
	lis = [ './command.sh']
	for line in lis:
        	stdin,stdout,stderr = ssh.exec_command(line)
        	print stdout
        	for lin in stdout:
                	print lin.strip()

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

	print "-------------------------------" + "\n" + " " +  IP + USERNAME

	scp (FILEPATH,SERVERPATH,IP,USERNAME,PASSWORD)
	ssh1 = ssh(IP,USERNAME,PASSWORD)


def usage():
	print """Usage:  -h: help. """



def main():
    try:
        opts, args = getopt.getopt(sys.argv[1:], ":", ["g="])
    except getopt.GetoptError, err:
        print "error"
        usage()
        sys.exit(2)

    for o, a in opts:
        if o in ('-g', 'g'):
            ssh1 = ssh(IP, USERNAME, PASSWORD)

if __name__ == "__main__":
     main()
