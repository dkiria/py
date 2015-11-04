#!/usr/bin/python
#-----------------------------------------
import git
import os
import getopt
import sys
from git import Repo
import re
#repo = git.Repo('.')
#print repo.git.status()

#----------------------------------------------------------



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

                tmp = repo.git.status()
                for ln in tmp.split('\n'):

                    if self.get_match1(ln) !=None:
                        print self.get_match1(ln)
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

    def get_match1(self, get_arg):
        mdict=(
                r'.*deleted: (.+)',
                r'.*modified: (.+)'
            #'del':'deleted',
            #'mod':'modified',
            );
        for value in mdict:
            m=re.match(value, get_arg)
#           print m
            if m:
                return m.group()
        return None



def usage():
    print """Usage: --help, -h: help. """
    print """       --gitstat, -g: gitstat. """

def main():

#   b = GitStatus()
#   b.git_s()

    try:
        opts, args = getopt.getopt(sys.argv[1:], "dg", ["gitstat=","gitdif="])
    except getopt.GetoptError, err:
usage()
        sys.exit(2)

    for o, a in opts:
        if o in ('-g', '--gistat'):
            repo = git.Repo('.')
            print repo.git.status()
            gitstat = a

            b = GitStatus()
            b.git_s()
        elif o in ('-d' , '--gitdif'):
            b=GitStatus()
            b.git_d()


if __name__ == "__main__":
    main()

