import sys
import re         # regular expression tools

if len(sys.argv) is not 3:
    print("Correct usage: wordCountTest.py <input file> <output file>")
    exit()

inputName = sys.argv[1]
outputName = sys.argv[2]
dict = {}

with open(inputName, 'r') as inputFile:
    for line in inputFile:
        line = line.replace(',', '')
        line = line.replace('.', '')
        # get rid of newline characters
        line = line.strip()
        # split line on whitespace and punctuation
        words = re.split('[ \t]', line)
        print(words)
        for word in words:
            if word.lower() in dict:
                dict[word.lower()] += 1
            else:
                dict[word.lower()] = 1
    inputFile.close()
for x in dict:
    print(dict[x])