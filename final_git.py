#!/usr/bin/python
#!/usr/bin/pythonimport git
import git
import os
import getopt
import sys
from git import Repo
import re
#repo = git.Repo('.')
#print repo.git.status()

class GitStatus:
    def git_s(self):
        res = 0
        tmp_repo = list()


        lis = list ()
        for line in open('.gitignore'):
            ldir = '/' +  line.rstrip('\n')
            lis.append(ldir)

        lis.append('/./')
        print "list "
        print  lis
        print "\n"
        for line in lis:

            path = os.getcwd() + line + '.git'
            path1 = os.getcwd() + line
            res = os.path.isdir(path)
            print path1
            print res

            if res  == True:

                repo = git.Repo(path)
#               print repo.description
        #       repo.getDatabaseName()
                tmp = repo.git.status()
                for ln in tmp.split('\n'):
                    if self.get_match1(ln) != None:
                        print self.get_match1(ln)
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

                '.*deleted: (.+)',
                '.*modified: (.+)',
                '#\t\w+\.*\w+'
            );
        for value in mdict:
            m=re.match(value, get_arg)

            if m:
                return m.group()
        return None

def usage():
    print """Usage: --help, -h: help. """
 print """       --gitstat, -g: gitstat. """

def main():


    try:
        opts, args = getopt.getopt(sys.argv[1:], "dg", ["gitstat=","gitdif="])
    except getopt.GetoptError, err:
        usage()
        sys.exit(2)

    for o, a in opts:
        if o in ('-g', '--gistat'):
            gitsta = a
            b = GitStatus()
            b.git_s()
        elif o in ('-d' , '--gitdif'):
            b=GitStatus()
            b.git_d()


if __name__ == "__main__":
     main()
                          
