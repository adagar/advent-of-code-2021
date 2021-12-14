import sys
 
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
transformations = {}
for i in range(0, steps):
  print("Step:", i)
  newStart = start[:]
  for j in range(0, len(start) - 1):
    pair = start[j] + start[j+1]
    # print(pair)
    if pair in rules:
      newStart.insert(j+1 + j, rules[pair])
      
  # print(start)
  transformations["".join(start)] = newStart
  print(transformations)
  start = newStart
      

# print(start,rules)
most = [mostCommon(start), start.count(mostCommon(start))]
least = [leastCommon(start), start.count(leastCommon(start))]

print(most, least, most[1] - least[1])

