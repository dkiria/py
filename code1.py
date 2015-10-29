#!/usr/bin/python
#-----------------------------------------
import git
import os
import getopt
import sys
from git import Repo
repo = git.Repo('.')
print repo.git.status()

#----------------------------------------------------------

git_ign = open('.gitignore')
git_ign.readlines()

#--------------------------------------------------------
print(os.path.isdir("/home/el"))
print(os.path.exists("/home/el/gitignore.txt"))

result = os.path.isdir("/home/el")
if result == False:
    print "error"
elif result == True:
    repo = git.Repo('.')
    print repo.git.status()
else:
    print "result fail"

def usage():
    print """Usage: --help, -h: help. """
    print """       --gitstat, -g: gitstat. """

def main():
    try:
        opts, args = getopt.getopt(sys.argv[1:], "g", ["gitstat="])
    except getopt.GetoptError, err:
        usage()
        sys.exit(2)

    for o, a in opts:
        if o in ('-g', '--gistat'):
            gitstat = a

if __name__ == "__main__":
    main()

