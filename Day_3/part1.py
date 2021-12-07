file = open('input.txt', 'r')
lines = file.readlines()

splitLines = [list(line) for line in lines]

gammaRate = []
epsilonRate = []
sums = [0] * (len(splitLines[0]) - 1)

for x in range(len(splitLines)):
  
  newReading = splitLines[x]
  print(newReading)
  
  for i in range(len(newReading) - 1):
    sums[i] += int(newReading[i])
    
for val in sums:
  if val > len(lines) / 2:
    gammaRate.append('1')
    epsilonRate.append('0')
  else:
    gammaRate.append('0')
    epsilonRate.append('1')

gammaInt = int("".join(gammaRate), 2)
epsilonInt = int("".join(epsilonRate), 2)

print(gammaInt * epsilonInt)
