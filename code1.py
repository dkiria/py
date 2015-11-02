

#!/usr/bin/python
#-----------------------------------------
import git
import os
import getopt
import sys
from git import Repo
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
                print repo.git.status()
            else:
                print "\n error \n"

def usage():
    print """Usage: --help, -h: help. """
    print """       --gitstat, -g: gitstat. """

def main():

    b = GitStatus()
    b.git_s()

    try:
        opts, args = getopt.getopt(sys.argv[1:], "g", ["gitstat="])
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
if __name__ == "__main__":
    main()
