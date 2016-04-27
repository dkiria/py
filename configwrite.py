#!/usr/bin/python
import ConfigParser
from ConfigParser import SafeConfigParser
Config = ConfigParser.RawConfigParser()
parser = SafeConfigParser()

def auto_write():

	Section=raw_input('Enter provider name : ')
	config.add_section(Section)
	Ip=raw_input('Enter host : ')
	config.set(Section, 'Host', Ip)
	User=raw_input('Enter username : ')
	config.set(Section, 'Username', User)
	Pass=raw_input('Enter password : ')
	config.set(Section, 'Password',Pass)

# Writing our configuration file to 'example.cfg'
	file_name=raw_input('Enter file name : ')
	with open(file_name, 'wb') as configfile:
    		config.write(configfile)


def write_cfg():

	# Add provider to the configfile

	#provider 1
	Config = ConfigParser.ConfigParser()
	Config.add_section('provider1')
	Config.set('provider1', 'name', 'Vodafone')
	Config.set('provider1', 'host', '192.168.1.254')
	Config.set('provider1', 'user', 'root')
	Config.set('provider1', 'passwd', 'ert4or3')
	#provider 2
	Config.add_section('provider2')
	Config.set('provider2', 'name', 'Voda')
	Config.set('provider2', 'host', '192.168.1.254')
	Config.set('provider2', 'user', 'root')
	Config.set('provider2', 'passwd', 'ert4or3')
	#provider3
	Config.add_section('provider3')
	Config.set('provider3', 'name', 'Ote')
	Config.set('provider3', 'host', '192.168.1.254')
	Config.set('provider3', 'user', 'root')
	Config.set('provider3', 'passwd', 'ert4or3')
	#Writing our configuration file to 'example.cfg'
	file_name=raw_input('Enter file name : ')
	with open(file_name, 'wb') as configfile:
		Config.write(configfile)

write_cfg()
