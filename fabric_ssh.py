#!/usr/bin/python
import fabric
from fabric.api import abort, cd,run, env, get,put, hide, hosts, local, prompt
import sys
def ssh(url, user, passwd,cmd):
    env.host_string = url
    env.user = user
    env.password = passwd
    print env.hosts
    print env.user
    print env.password
    run(cmd)
    put('command.sh.py', '/root')
#    run('./command.sh')

def main():
    url = '192.168.1.254'
    user = 'root'
    passwd = 'shitNobrod'
    cmd = 'ls'

    try:
        connect = sys.argv[1]
    except IndexError:
        print ("No file.")
        exit(1)

    connect = ssh(url,user,passwd,cmd)

if __name__ == "__main__":
    main()
