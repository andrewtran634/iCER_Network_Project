import sys
import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt

def makeHistogram(numbers, lines):

#numbers is the array that comes in, lines is the number of nodes that are tested (the number of lines in the .csv file)

    plt.hist(numbers, lines / 3)
    plt.xlabel('Avg Seconds')    
    plt.ylabel('Number of Nodes')
    plt.show()

def processFile(filename):
    numbers = [] #holds all the averages of all the nodes
    count = 0		#counts all the nodes tested
    try:
        with open(filename, 'r') as inputFile:
            for line in inputFile:
                count += 1
                line = line.strip()    
                line = line.split(',')
                time = 0
                divide = 0		#need these two variables to make some averages
                for x in range(len(line)):
                    try:
                        line[x] = float(line[x])	#if something in the .csv file is a number, convert it
                        time += line[x]
                        divide += 1
                    except:
			line[x] = line[x]		#if something in the .csv file isn't a number, don't do anything
                
                numbers.append(time/divide)	#appends an average to the numbers list
    except IOError:
        print 'File failed to open'
    makeHistogram(numbers, count)		#actually makes the histogram	

def main(argv):
    theFile = raw_input('What is the file name? ')  #this is supposed to be where all the testing data is stored
    processFile(theFile)
    
if __name__ == "__main__":
    main(sys.argv)


