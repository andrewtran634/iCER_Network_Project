import os
import sys

writeTo = raw_input('Where do you want to write to? ') #this should be the name of the .csv file where you want all the info to go

extension = raw_input('What kind of nodes are they? [scw, nvx, icx, all] ')
	#this should be the name of the node i.e. 'scw', 'icx', 'ifi', 'csm' or whatever (you can also just put in 'all')
extension = extension.split()
#print extension
duplicate = False
for i in os.listdir(os.getcwd()):
    rightOne = False
    if i.endswith('.csv'):
	read = i
	i = i.split('-')
	if extension != 'all':
	    #extension = extension.split()
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
