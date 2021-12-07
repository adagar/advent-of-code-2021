file = open('input.txt', 'r')
lines = file.readlines()

count = 0
temp = lines[0]
lineCounter = 0;

for line in lines:
    if line > temp:
      count += 1
      print("Increase!")
    temp = line
    lineCounter += 1
    print(temp)
    
    
print(lineCounter)
