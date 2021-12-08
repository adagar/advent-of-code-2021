import sys
fileName = sys.argv[1]

def parseMyFile(file):
  fileData = open(file, "r")
  lines = fileData.readlines()
  
  entries = []
  for line in lines:
    output = line.replace("\n", "").split(" | ")
    print(output)
    entries.append(output[1].split(" "))
      
  return entries
    
digits = {1: 0,
          4: 0,
          7: 0,
          8: 0}

entries = parseMyFile(fileName)
for entry in entries:
  for signal in entry:
    numSegments = len(signal)
    if numSegments == 2:
      digits[1] += 1
    elif numSegments == 3:
      digits[7] += 1
    elif numSegments == 4:
      digits[4] += 1
    elif numSegments == 7:
      digits[8] += 1

sum = 0
for key in digits:
  sum += digits[key]
  
print(sum)
