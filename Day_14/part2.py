import sys
from collections import Counter
 
fileName = sys.argv[1]
steps = int(sys.argv[2])

def parseMyFile(file):
  fileData = open(file, "r")
  lines = fileData.readlines()
  
  start = [char for char in lines[0].strip()]
  rules = {}
  
  for line in range(2, len(lines)):
    rule = lines[line].strip().split(" => ")
    rules[lines[line].strip().split(" -> ")[0]] = lines[line].strip().split(" -> ")[1]
    
  return start, rules
  
def mostCommon(arr):
  return max(set(arr), key=arr.count)
  
def leastCommon(arr):
  return min(set(arr), key=arr.count)
  
start, rules = parseMyFile(fileName)

def transform(start):
  newStart = []
  
  for j in range(0, len(start) - 1):
    pair = start[j] + start[j+1]
    newTrypt = [start[j], rules[pair]]
    # print(newTrypt)
    newStart.extend(newTrypt)
  newStart.append(start[-1])
  
  return newStart

def getPairs(start):
  pairs = []
  for i in range(0, len(start) - 1):
    pairs.append(start[i] + start[i+1])
  return pairs
pairs = getPairs(start)

pairCount = Counter(pairs)

for i in range(0, steps):
  updatedPairCount = {}
  for key in pairCount:
    newMiddle = rules[key]
    left = key[0] + newMiddle
    right = newMiddle + key[1]
    
    if(left in updatedPairCount):
      updatedPairCount[left] += pairCount[key]
    elif(left not in updatedPairCount):
      updatedPairCount[left] = pairCount[key]
    if(right in updatedPairCount):
      updatedPairCount[right] += pairCount[key]
    elif(right not in updatedPairCount):
      updatedPairCount[right] = pairCount[key]
        
  pairCount = updatedPairCount.copy()

print(pairCount)
newString = ""
alphaCount = {}
for key in pairCount:
  left = key[0]
  right = key[1]
  if(left in alphaCount):
    alphaCount[left] += pairCount[key]
  elif(left not in alphaCount):
    alphaCount[left] = pairCount[key]
  # if(right in alphaCount):
  #   alphaCount[right] += pairCount[key]
  # elif(right not in alphaCount):
  #   alphaCount[right] = pairCount[key]
  
print(alphaCount)
maxKey = max(alphaCount, key=alphaCount.get)
minKey = min(alphaCount, key=alphaCount.get)
# most = [mostCommon(newString), newString.count(mostCommon(newString))]
# least = [leastCommon(newString), newString.count(leastCommon(newString))]

print("".join(start))
# print(most, least, most[1] - least[1])
print(maxKey, alphaCount[maxKey], minKey, alphaCount[minKey])
print(alphaCount[maxKey] - alphaCount[minKey])

