import sys

#THIS FILE AUTOMATICALLY RUNS WHEN YOU ARE RUNNING pingCnode2Dev, or one of the pingNode2Node....qsub files


readFrom = sys.argv[1]		#this is the .txt file that is storing all the ping data
writeTo = sys.argv[2]		#this is the .csv file that will store the ping data in a more readable form
name = sys.argv[3]		#this is the header for each line of ping times
time = ''			#this is the variable that holds the time of an individual ping
date = False			#these bools are all markers that let the program know when the parsing needs to collect certain information
usage = False
usage2 = False
cpus_pinger = False
cpus_pingee = False
with open(writeTo, 'a') as writeFile:
    writeFile.write(name)
    writeFile.write(',')
    with open(readFrom, 'r') as readFile:
        for line in readFile:
            if usage or usage2:
                line = line.strip()
                line = line.split(',')
            else:
                line = line.split()
            if line:
                if date:
                    writeFile.write('DATE: ')
                    for z in line:
                        writeFile.write(z)			#collects the date and puts it in the "writeTo" file
                        writeFile.write(' ')
                    date = False
                    writeFile.write(',')
                if usage:
                    writeFile.write('USAGE OF PINGER: ')	#collects the usage of the pinging node and puts it in the "writeTo" file
                    for i in range(len(line)):
                        writeFile.write(line[i])
                    usage = False
                    writeFile.write(',')
		if usage2:
		    writeFile.write('USAGE OF PINGEE: ')	#collects the usage of the node pinged to node and puts it in the "writeTo" file
		    for a in range(len(line)):
		        writeFile.write(line[a])
		    usage2 = False
                    writeFile.write(',')
		if cpus_pinger:
		    writeFile.write("PINGER CPU'S: ")		#collects the number of cores of the pinging node and puts it in the "writeTo" file
		    writeFile.write(line[0])
		    cpus_pinger = False
		    writeFile.write(',')	
		if cpus_pingee:
		    writeFile.write("PINGEE CPU'S: ")		#collects the number of cores of the pinged to node and puts it in the "writeTo" file
		    writeFile.write(line[0])
		    cpus_pingee = False
                    writeFile.write(',')

                if line[0] == 'DATE':
                    date = True
                if line[0] == 'PINGER':
                    usage = True
		if line[0] == 'PINGEE':
		    usage2 = True			#whenever the program reaches these points in the readFrom file, a bool marker will go off
							#letting the program know that data will need to be collected and written to the writeTo file
		if line[0] =='PINGER-CPUS':
		    cpus_pinger = True
		if line[0] =='PINGEE-CPUS':
		    cpus_pingee = True
		
		
            
                if line[0] == '64':
                    word = line[7]
                    time = ''				#this place in the readFrom file is where the actually ping time is
							#program will go through, identify the time, and write it to the writeTo file
                    for x in range(len(word)):
                        if (word[x] >= '0' and word[x] <= '9') or word[x] == '.':
                            time += word[x]
                    writeFile.write(time)
                    writeFile.write(',')
        writeFile.write('\n')
