#!/bin/bash

echo  Hello $1 $2

echo "Bash Bash Bash"

if [ ${1,,} =  julien ] ; then 
	echo "great"
elif [ ${1,,} = help ] ; then
	echo "enter username"
else
	echo "idk"
fi

