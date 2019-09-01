#Alonso Granados
#Assignment 1
import sys

if len(sys.argv) is not 3:
    print("Correct usage: wordCountTest.py <input file> <output file>")
    exit()

inputName = sys.argv[1]
outputName = sys.argv[2]
dict = {}

with open(inputName, 'r') as inputFile:
    for line in inputFile:
        #Removes punctuation from line
        line = line.replace(',', ' ')
        line = line.replace(':', ' ')
        line = line.replace(';', ' ')
        line = line.replace('.', ' ')
        line = line.replace('-', ' ')
        line = line.replace('\'', ' ')
        line = line.replace('\"', ' ')
        #Removes EOL
        line = line.strip()
        #Checks for empty line
        if line == '':
            continue
        #Split line on whitespace
        words = line.split()
        #Count words
        for word in words:
            if word.lower() in dict:
                dict[word.lower()] += 1
            else:
                dict[word.lower()] = 1
    inputFile.close()

#Sort Alphabetical
sortedDict = sorted(dict)
with open(outputName, 'w') as outputFile:
    for x in sortedDict:
        outputFile.write("{} {}\n".format(x, dict[x]))
