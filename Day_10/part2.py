from os import error
import sys
from termcolor import colored
import math

fileName = sys.argv[1]

def parseMyFile(file):
  fileData = open(file, "r")
  lines = fileData.readlines()
  dataLines = []
  
  for line in lines:
    dataLines.append(line.strip())
  return dataLines
  
def removeMatches(line, pair):
  found = False
  
  while(pair in line):
    line = line.replace(pair, "")
    found = True
 
  return line

  
lines = parseMyFile(fileName)
pairs = ["()", "[]", "{}", "<>"]
closers = {")": 1, "]": 2, "}": 3, ">": 4}
openers = {"(":")", "[": "]", "{": "}", "<": ">"}
errorScores = []

cleanLines = []

for line in lines:
  # print("Starting line", line)
  dirty = True
  i = 0
  
  errorScore = 0
  
  while i < len(pairs):
    cleanedLine = removeMatches(line, pairs[i])
    # print(cleanedLine + "\n" + line)
    if(line != cleanedLine):
      # print("Found a match for", pairs[i])
      line = cleanedLine
      i = 0
    else:
      i += 1
      
  unpaired = line
  for opener in openers:
    # print(opener)
    unpaired = unpaired.replace(opener, "")
    # print(unpaired)
  if(len(unpaired) == 0):
    # errorScore += closers[line[0]]
    print(line, "is a valid but unpaired set")
    test = ""
    for j in reversed(range(len(line))):
      char = line[j]
      errorScore *= 5
      errorScore += closers[openers[char]]
      test += openers[char]
    print (test)
    errorScores.append(errorScore)
  # print("Ending line", line)
        
  
errorScores.sort()
print(errorScores)
print(errorScores[math.floor(len(errorScores) / 2)])
