import sys

readFrom = raw_input("What's the name of the file to read from? ")
writeTo = raw_input("What's the name of the file to write to? ")
name = raw_input("What's the name of the header? ")
time = ''
date = False
usage = False
with open(writeTo, 'a') as writeFile:
    writeFile.write(name)
    writeFile.write(',')
    with open(readFrom, 'r') as readFile:
        for line in readFile:
            if usage:
                line = line.strip()
                line = line.split(',')
            else:
                line = line.split()
            if line:
                if date:
                    writeFile.write('DATE: ')
                    for z in line:
                        writeFile.write(z)
                        writeFile.write(' ')
                    date = False
                    writeFile.write(',')
                if usage:
                    writeFile.write('USAGE: ')
                    for i in range(len(line)):
                        writeFile.write(line[i])
                    usage = False
                    writeFile.write(',')
                    
                if line[0] == 'DATE':
                    date = True
                if line[0] == 'LOAD':
                    usage = True
            
                if line[0] == '64':
                    word = line[7]
                    time = ''
                    for x in range(len(word)):
                        if (word[x] >= '0' and word[x] <= '9') or word[x] == '.':
                            time += word[x]
                    writeFile.write(time)
                    writeFile.write(',')
        writeFile.write('\n')
