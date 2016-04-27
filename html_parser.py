#!/usr/bin/python3
from selenium.webdriver.common.keys import Keys
import urllib
try:
    import configparser
except:
    from six.moves import configparse
import re
import sys
#from urllib2 import Request, urlopen, URLError, HTTPError
import requests
from selenium import webdriver
from bs4 import BeautifulSoup
from lxml import html
import subprocess
from subprocess import call
import fabric
#import binaries.genpasswd
#rom fabric.api import abort, cd, env, get, hide, hosts, local, prompt, \
#    put, require, roles, run, runs_once, settings, show, sudo, warn
#rom fabric.contrib.console import confirm

def read_conf():

    Config = configparser.ConfigParser()
    try:
        input = raw_input
    except NameError:
        pass
    config_file = (input("configfile: "))
#onfig_file = raw_input("configfile: ")
    Config.read(config_file)
    Config.sections()
    print (Config.sections())
    try:
        input = raw_input
    except NameError:
        pass
    provider = (input("provider "))

#provider = raw_input("provider: ")
read_conf()
def ConfigSectionMap(section):
    dict1 = {}
    options=Config.options(section)
    for option in options:
            try:
                dict1[option] = Config.get(section, option)
                if dict1[option] == -1:
                    DebugPrint("skip: %s" % option)
            except:
                print("exception on %s!" % option)
                dict1[option] = None
    url =( dict1['host'])
    user_ssh = dict1['user_ssh']
    passwd_ssh = dict1['passwd_ssh']
    gen_seed = dict1['gen_seed']
    return url, user_ssh, passwd_ssh,gen_seed

url,user_ssh,passwd_ssh, gen_seed  = ConfigSectionMap(provider)
print ("ip : " + url + ",  username : " +  user_ssh + ",  password : " + passwd_ssh + ", seed : " + gen_seed)
#connect 2 web interface (user)
user = 'user'
password = 'user'
r  = requests.get("http://" +url + "/open/sys_info.cgi?type=all-params",auth=(user, password))
data = r.text
print (data)
soup = BeautifulSoup(data)
#match serial and fw name

def get_serial(get_arg):
        mdict=(
		"\d{3}[-.]?\d{3}[-.]?\d{6}",
		'[a-z]+',
                );
        for value in mdict:
            m=re.match(value, get_arg)
            if m:
                print ('find match')
                serial1=m.group()
                print ("serial number is : " + serial1)
                serial = '158605000106'
                cmd_str = './binaries/genpasswd -m 2 -s ' + gen_seed + ' -l ' + serial + ' -n 10'
                print ('Admin Pass : ')
                subprocess.call(cmd_str, shell=True)
                print ('\n')
#	    return m.group()
                return None

get_serial(data)

user = 'admin'
password = 'admin'
try:
	r  = requests.get("http://"  +url + "/cgi-bin/page.pl?type=system&page=local",auth=(user, password))
	print ("Board is unlock")
except:
	print ("url error")

def ssh(url, user, passwd):
        #env.hosts = url
        env.user = user_ssh
        env.password = passwd_ssh
        env.host_string = url
        run('df')

#ssh(url, user_ssh, passwd_ssh)

