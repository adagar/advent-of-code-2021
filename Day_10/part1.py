from os import error
import sys
from termcolor import colored
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
closers = {")": 3, "]": 57, "}": 1197, ">": 25137}
openers = ["(", "[", "{", "<"]
errorScore = 0

cleanLines = []

for line in lines:
  print("Starting line", line)
  dirty = True
  i = 0
  
  while i < len(pairs):
    cleanedLine = removeMatches(line, pairs[i])
    print(cleanedLine + "\n" + line)
    if(line != cleanedLine):
      print("Found a match for", pairs[i])
      line = cleanedLine
      i = 0
    else:
      i += 1
  for opener in openers:
    line = line.replace(opener, "")
  if(len(line) > 0):
    errorScore += closers[line[0]]
  print("Ending line", line)
        
  

print(errorScore)
