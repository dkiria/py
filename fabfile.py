#!/usr/bin/python
#!  /usr/bin/env python
import ConfigParser
import sys
import os
from ConfigParser import SafeConfigParser
from fabric.api import abort, cd, env, get, hide, hosts, local, prompt, \
    put, require, roles, run, runs_once, settings, show, sudo, warn
from fabric.contrib.console import confirm
from getpass import getpass
from ConfigParser import SafeConfigParser
#Set host
env.hosts = [
    'enter your ip'
    ]

# Set the username
env.user   = "enter username"


# Set the password
env.password = "enter password"


#set host ,pass, user from configfile

def parser():
	parser = SafeConfigParser()
	config_file = raw_input("configfile: ") # doesnt matter if we echo username so use raw_input()
	parser.read(config_file)


	for section_name in parser.sections():
        	print 'Section:', section_name
        	print '  Options:', parser.options(section_name)
        	env.hosts =parser.get(section_name, 'ip')
        	print env.hosts
        	env.user=parser.get(section_name, 'user')
        	print env.user
        	env.password =parser.get(section_name, 'password')
        	print env.password
        	print

        	local('ls')
        	run('ls')



def echo():
      run("echo -n 'Hello, you are tuned to Tecmint ' ")


def host_type():
    run('uname -s')
    
def diskspace():
    run('ls')
    run( 'df')
    run("git status")

def hello():
    print("Hello world!")

def prepare_deploy():
    local("./command.sh")
    local("df")

def new_user(username, admin='no', comment="No comment provided"):
    print("New User (%s): %s" % (username, comment))
    pass

def test():
    local("df")

def commit():
        local("git add -p && git commit")

def push():
        local("git push")

def status():
        local ("git status")

def prepare_deploy():
        test()
        commit()
        push()
