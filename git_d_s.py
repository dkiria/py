#!/usr/bin/python

import git
import os
import getopt
import sys
from git import Repo

#repo=git.Repo('.')
#t = repo.head.commit.tree
#repo.git.diff(t)
#repo.git.diff('HEAD~1')
#print repo.git.diff(t)

class GitStatus:
    def git_s(self):
        print "opengitignore " + "\n"
        for line in open('.gitignore'):

            ldir ='/' +  line.rstrip('\n')
            path=os.getcwd() + ldir
            print path + "\n"
            result = os.path.isdir(line.rstrip('\n'))
            if result == True:
                repo = git.Repo(line.rstrip('\n'))
                print repo.git.status()
            else:
                print "\n error \n"
    def git_d(self):
        print "opengitignore " + "\n"
        for line in open('.gitignore'):
            ldir ='/' +  line.rstrip('\n')
            path=os.getcwd() + ldir
            print path + "\n"
            result = os.path.isdir(line.rstrip('\n'))
            if result == True:
                repo = git.Repo(line.rstrip('\n'))
                print repo.git.diff()
else:
                print "\n error \n"

def usage():
    print """Usage: --help, -h: help. """
    print """       --gitstat, -g: gitstat. """
def main():


    try:
        opts, args = getopt.getopt(sys.argv[1:], "dg", ["gitdif=","gitstat="])
    except getopt.GetoptError, err:
            usage()
            sys.exit(2)
    for o, a in opts:
        if o in ('-d', '--gitdif'):
            repo=git.Repo('.')
            t = repo.head.commit.tree
            print repo.git.diff()
            b =  GitStatus()
            b.git_d()

        elif o in ('-g', '--gitstat'):
            b = GitStatus()
            b.git_s()


if __name__ == "__main__":
    main()
