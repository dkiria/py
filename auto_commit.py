#!/usr/bin/python
import git
import subprocess
import os
import getopt
import sys
from git import Repo
import re
import shutil
import time


###########################------gitadd----############################################################
def gitAdd(fileName):
	cmd = 'git add ' + fileName
	pipe = subprocess.Popen(cmd, shell=True, stdout = subprocess.PIPE,stderr = subprocess.PIPE )
	(out, error) = pipe.communicate()
	print out,error
	pipe.wait()
#	path = os.getcwd()
	return
###########################----git commit----#############################################################

def gitCommit(commitMessage):
	cmd = 'git commit -am "%s"'%commitMessage
	pipe = subprocess.Popen(cmd, shell=True,stdout = subprocess.PIPE,stderr = subprocess.PIPE )
	(out, error) = pipe.communicate()
	print out,error
	pipe.wait()
	return
############################----git push----################################################################

def gitPush():
	cmd = 'git push '
	pipe = subprocess.Popen(cmd, shell=True,stdout = subprocess.PIPE,stderr = subprocess.PIPE )
	(out, error) = pipe.communicate()
	pipe.wait()
	return
#############################################################################################################
str = raw_input("Enter file  name: "+ "\n");
gitAdd(str)
print "git add---> ok "
str = raw_input("Enter your commit: "+ "\n");
gitCommit(str)
print "git commit---> ok "
gitPush()


