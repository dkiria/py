#!/bin/bash
echo "Hello, "$USER".   "
echo "Bash version ${BASH_VERSION}..."

command_list()
{
	ls
	ls -l
	ps
	df
}


counter(){
	for (( c=1; c<=5; c++ ))
	do
   		echo "Welcome $c times"
	done
}

command_list
