#!/usr/bin/python
#!/usr/bin/pythonimport git
import git
import os
import getopt
import sys
from git import Repo
import re
import subprocess
#git rebase
class Gitrm:
	def git_r(self):
		try:
			repo = git.Repo('.')
			str = raw_input("Enter file name: ");
			print "git rm : ", str
			repo.git.rm( str )
		except git.exc.GitCommandError as e:
			git_usage()
#git add
class GitAdd:
	def git_ad(self):
		try:
			def gitAdd(fileName, repoDir):

				cmd = 'git add ' + fileName
				pipe = subprocess.Popen(cmd, shell=True, cwd=repoDir,stdout = subprocess.PIPE,stderr = subprocess.PIPE )
				(out, error) = pipe.communicate()
				print out,error
				pipe.wait()
				return
		except git.exc.GitCommandError as e:
				git_usage()

		path = os.getcwd()
		print "\n  Working directory is : " +  path + "\n"
		repoDir = raw_input("Enter repo name: "+ "\n");
		str = raw_input("Enter file  name: "+ "\n");
		gitAdd(str,repoDir)
		print "git add---> ok "


	def git_c(self):

		def gitCommit(commitMessage, repoDir):
			cmd = 'git commit -am "%s"'%commitMessage
			pipe = subprocess.Popen(cmd, shell=True, cwd=repoDir,stdout = subprocess.PIPE,stderr = subprocess.PIPE )
			(out, error) = pipe.communicate()
			print out,error
			pipe.wait()
			return

		str = raw_input("Enter your commit: "+ "\n");
		gitCommit(str, repoDir)
		print "git commit---> ok "

#git pull
class GitPull:
	def git_p(self):
		res=0
		tmp_repo = list()
		lis = list()
		try:
			for line in open('.gitignore'):
				if line != '\n':
					ldir = '/'+line.rstrip('\n')
					lis.append(ldir)

			lis.append('/')
			suc_list = list()
			err_list =list()
			for line in lis:
				path = os.getcwd() + line + '.git'
			 	path1 = os.getcwd() + line
			 	res = os.path.isdir(path)
			 	if res  == True:
					 print "\n" + path1
					 try :
						repo = git.Repo(path)
					 	tmp= repo.git.pull()
					 	print tmp
					 	suc_list.append(path1)
					 except git.exc.GitCommandError as e:
						err_list.append(path1)
						git_usage()
						continue
					 def get_match1(self, get_arg):
						 mdict=(
								 '.*deleted: (.+)',
								 '.*modified: (.+)',
								 '#\t\w+\.*\w+(.+)'
								);
					 	 for value in mdict:
							 m=re.match(value, get_arg)
							 if m:
								 return m.group()
					 	 return None



			print"\n sucess : "+str(suc_list) + "\n failed : " +  str(err_list)
		except IOError as e:
			    print "I/O error({0}): {1}".format(e.errno, e.strerror)


class GitStatus_diff:
#git status
	def git_status(self):
		tmp_repo = list()

		lis = list ()
		try:
			for line in open('.gitignore'):

				if line != '\n':

					ldir = '/'+line.rstrip('\n')
					lis.append(ldir)

# '/' or '.' ----> home dir

			lis.append('/')
			for line in lis:
				path = os.getcwd() + line + '.git'
				path1 = os.getcwd() + line
				res = os.path.isdir(path)
		#	print path
		#	print res
				if res	== True:
					print  "\n" + path1
					f1 = open("status.patch", "wb")
					repo = git.Repo(path)
					tmp = repo.git.status()
					f1.write(repo.git.status())
					f1.close
					for ln in tmp.split('\n'):
						if self.get_match1(ln) != None:
							print self.get_match1(ln)
		except IOError as e:
			print "I/O error({0}): {1}".format(e.errno, e.strerror)

#git diff
	def git_diff(self):
		print "opengitignore " + "\n"
		try:
			for line in open('.gitignore'):
				if line != '\n':
					ldir ='/' +  line.rstrip('\n')
					path=os.getcwd() + ldir
					print path + "\n"
					result = os.path.isdir(line.rstrip('\n'))
					if result == True:
						repo = git.Repo(line.rstrip('\n'))
						print repo.git.diff()
						fo = open("diff.patch", "wb")
						fo.write(repo.git.diff())
						fo.close
					else:
						print "\n error \n"

				elif line == '\n':
					print "empty"
		except IOError as e:
			print "I/O error({0}): {1}".format(e.errno, e.strerror)



	def get_match1(self, get_arg):
		mdict=(
				'.*deleted: (.+)',
				'.*modified: (.+)',
				'#\t\w+\.*\w+(.+)'
				);
		for value in mdict:
			m=re.match(value, get_arg)
			if m:
				return m.group()
		return None

def git_usage():
	print "git  error"

def usage():
	print """Usage:  -h: help. """
	for line in open('manual_getsta.txt'):
		ldir = line.rstrip('\n')
		print ldir


def main():


	try:
		opts, args = getopt.getopt(sys.argv[1:], "dpghar", ["gitstatus=","gitpull=","gitdiff=","help=","gitadd=","gitrm="])
	except getopt.GetoptError, err:
		print "error"
		usage()
		sys.exit(2)

	for o, a in opts:
		if o in ('-g', '--gistatus'):
			gitsta = a
			b = GitStatus_diff()
			b.git_status()

		elif o in ('-a' , '--gitadd'):
			b=GitAdd()
			b.git_ad()
			b.git_c()


		elif o in ('-r' , '--gitrm'):
			b=Gitrm()
			b.git_r()

		elif o in ('-p' , '--gitpull'):
			b=GitPull()
			b.git_p()
		elif o in ('-d' , '--gitdiff'):
			b=GitStatus_diff()
			b.git_diff()
		elif o in ('-h', '--help'):
			print "\n"
			print "             help              "
			for line in open('manual_getsta.txt'):
				ldir = line.rstrip('\n')
				print ldir


if __name__ == "__main__":
	 main()
