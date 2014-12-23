import os
import sys

writeTo = sys.argv[1]		#this should be the name of the .csv file where you want all the info to go
extension = sys.argv[2]		#this should be the name of the node i.e. 'scw', 'icx', 'ifi', 'csm' or whatever (you can also just put in 'all')
extension = extension.split()
duplicate = False
for i in os.listdir(os.getcwd()):		#searches through directory
    rightOne = False
    if i.endswith('.csv'):
	read = i
	i = i.split('-')
	if extension != 'all':
	    for x in extension:		#if input isn't 'all', it will look for the files that have the same node name as extension 
		for a in i:
	            if x == a:
			rightOne = True 
	
	else:
	    rightOne = True
	if rightOne:
     	    with open(read, 'r') as inputFile:		#then the program will write the contents of the 'right' to the writeTo .csv file
            	for line in inputFile:
               	    with open(writeTo, 'a') as written:
                        written.write(line)
