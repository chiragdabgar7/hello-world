#!/bin/bash
echo "Hey this is a script"
echo 
echo "Welcome to the Main Menu"
echo "..."
while :
do
	echo "Would you like to begin?  (y/n)"
	read in
	case $in in
	y|Y|Yes|YES|yes) echo "You chose yes";;
#	*[[:alnum:]]*) echo "You entered an alpha num char";;
	[[:alpha:]]) echo "You chose an alphabet";;
	n|N|No|NO|no) echo "You chose no";;
	quit|q) break ;;
	esac
done
echo "out of the while loop"
echo $in
