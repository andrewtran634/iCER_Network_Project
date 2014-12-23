import sys
import math
    
def processFile(filename):
    writeTo = sys.argv[2]	#this is the name of the list of bad nodes, make it whatever you want
    if len(sys.argv) > 3:
    	times = sys.argv[3]		#this is how many standard deviations away you think is a good threshold for deciding which is a bad node
    else:
	times = '3'			#if no input, default will be 3 standard deviations


    nodeAverages = []			#bunch of lists to store average data, usage data, node names, and dates
					#nodeLoadAvgsPingers and nodeLoadAvgsPingers are actually lists of lists. for every node, there are three numbers 
						#given for uptime, so nodeLoadAvgsPingers/Pingees acts as a list of these three number lists for each node
    nodeLoadAvgsPingers = []
    nodeLoadAvgsPingees = []
    nodeNames = []
    dates = []
    hugeAverage = 0
    standDev = 0
    pinger_cpus = 12
    pingee_cpus = 12		#if data on the number of cores isn't available when compiling list of bad nodes, default number of cores will be 12
    try:
        with open(filename, 'r') as inputFile:
            for line in inputFile:
                line = line.strip()    
                line = line.split(',')
                time = 0
                divide = 0
                
                loadAveragePinger = []	#these two lists hold the data collected from "uptime" on the pinging node and the node that is getting pinged to
                loadAveragePingee = []
                for x in range(len(line)):
                    if x == 0:
                        nodeNames.append(line[x])	#append the name to the nodeNames list
                    else:
                        try:
                            line[x] = float(line[x])
                            time += line[x]		#if there's a number in the line, convert it
                            divide += 1
                        except:
                            usage = line[x]
                            usage = usage.split()
                            if usage and usage[0] == 'DATE:':
                                dates.append(usage[4])		#appends date to date list
                            elif usage and usage[0] == 'USAGE' and usage[2] == 'PINGER:':
                                reachedAverage = False
                                for x in range(len(usage)):
                                    if reachedAverage == True:
                                        usage[x] = float(usage[x])		#finds uptime info of the pinging node in the .csv file and 
										#appends it to the loadAveragePinger list	
                                        loadAveragePinger.append(usage[x])
                                    elif usage[x] == 'average:':
                                        reachedAverage = True
                                    
                            elif usage and usage[0] == 'USAGE' and usage[2] == 'PINGEE:':
                                reachedAverage = False
                                for x in range(len(usage)):			#finds uptime info of the node getting pinged to in the .csv file and
										#and appends it to the loadAveragePinger list
                                    if reachedAverage == True:
                                        usage[x] = float(usage[x])
                                        loadAveragePingee.append(usage[x])
                                    elif usage[x] == 'average:':
                                        reachedAverage = True
			    elif usage and usage[0] == 'PINGER':
				usage[2] = int(usage[2])
				pinger_cpus = usage[2]
			    elif usage and usage[0] == 'PINGEE':		#finds number of cores of both the pinging node and the node getting 
										#pinged to, and sets pinger_cpus and pingee_cpus to these numbers
				usage[2] = int(usage[2])
				pingee_cpus = usage[2]
				


                                           
                nodeLoadAvgsPingers.append(loadAveragePinger)		#appends uptime data for pinging node and pingee node to there respective list of lists
                nodeLoadAvgsPingees.append(loadAveragePingee)
      
                nodeAverages.append(time / divide)		#appends average for each node pinging to the nodeAverages list
            hugeAverage = sum(nodeAverages) / len(nodeAverages)		#at the end, sum up all the averages and divides it by the number of nodes tested in a file
										#and this becomes the huuuge average of the .csv file	
            
            for i in nodeAverages:
                standDev += (i - hugeAverage)**2	#finds the variation in the .csv file
            standDev /= len(nodeAverages)		#calculates standard deviation
    except IOError:
        print 'File failed to open'
    try:
        with open(writeTo, 'a') as writing:
            writing.write(filename)
            writing.write('\n')
            writing.write('Average of all nodes: ')
            writing.write(str(hugeAverage))
            writing.write('\n')
            writing.write('Standard Deviation times ')
            writing.write(times)
            writing.write(': ')
            writing.write(str(standDev * int(times)))
            writing.write('\n')
            writing.write('\n')
            for a in range(len(nodeAverages)):
                tooHighPinger = False
                tooHighPingee = False
                if nodeAverages[a] > hugeAverage + (standDev * int(times)): 	#if a node's average is greater than the 
											#huge average + the standard deviation * some number
												#we start to check the usage
                    theLoadPinger = nodeLoadAvgsPingers[a]
                    theLoadPingee = nodeLoadAvgsPingees[a]
                    for x in theLoadPinger:
                        if x / (pinger_cpus - 1) > 0.5:			
                            tooHighPinger = True
                            break				#----HEYHEYHEY DIRK, THIS COMMENT IS REALLY IMPORTANT----		
								#if any of the numbers gathered from uptime data / by the number of cores on a node
								#is greater than 0.5, I mark the node as having too high of a load average to be 
								#considered viable
                    for y in theLoadPingee:
                        if y / (pingee_cpus - 1) > 0.5:			
                            tooHighPingee = True
                            break    					
                    if tooHighPinger == False and tooHighPingee == False:
                        writing.write('\n')
                        writing.write(nodeNames[a])
                        writing.write('\n')
                        writing.write('Node Average: ')
                        writing.write(str(nodeAverages[a]))
                        writing.write('\n')
                        writing.write('Load Average Pinger: ')
                        writing.write(str(theLoadPinger))
                        writing.write('\n')
                        writing.write('Load Average Pingee: ')
                        writing.write(str(theLoadPingee))
                        writing.write('\n')
                        writing.write('Time: ')
                        writing.write(str(dates[a]))
                        writing.write('\n')
                        writing.write('\n')
                        writing.write('\n')
    except IOError:
        print 'File failed to open'
def main(argv):
    fileName = sys.argv[1]  #this is supposed to be where all the testing data is stored
    processFile(fileName)

if __name__ == "__main__":
    main(sys.argv)


            
                    

