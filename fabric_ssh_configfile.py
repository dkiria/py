#!/usr/bin/python
import ConfigParser
import getpass
import getopt
import sys
from fabric.api import abort, cd, env, get, hide, hosts, local, prompt, \
    put, require, roles, run, runs_once, settings, show, sudo, warn
from fabric.contrib.console import confirm
from getpass import getpass
from ConfigParser import SafeConfigParser
from ConfigParser import SafeConfigParser

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

def ssh(ip, user, passwd, exec_script, serverpath = '~/'):
        #env.hosts = ip
        env.user = user
        env.password = passwd
        env.host_string = ip

	try:
		if exec_script == ' ':
			print 'error'
		else:
			print "exec_script is None"
        except IndexError:
                print "No file found"
        else:
		put(exec_script, serverpath)
		out = run(serverpath + exec_script)

def main():
        i = 1
        var = 1

        try:
                config_file = sys.argv[1]
        except IndexError:
                print "No config file."
                exit(1)

        while var == 1:
                name = get_cfg_value(config_file, 'pc' + str(i), 'name', 'yes')
                if name == None:
                    break
                ip = get_cfg_value(config_file, 'pc' + str(i), 'ip', 'yes')
                user = get_cfg_value(config_file, 'pc' + str(i), 'username', 'yes')
                passwd = get_cfg_value(config_file, 'pc' + str(i), 'pass', 'yes')
                exec_script = get_cfg_value(config_file, 'pc' + str(i), 'exec_script', 'yes')
                serverpath = get_cfg_value(config_file, 'pc' + str(i), 'server_path', 'no')
                i = i + 1
		try:
                	ssh(ip, user, passwd, exec_script, serverpath)
		except NetworkError:
			print  sys.exc_type
#			local('mail -s "exception  dkiria@oxygenbroadband.com < /dev/null ')

if __name__ == "__main__":
        main()
