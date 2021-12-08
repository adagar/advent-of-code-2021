import sys
fileName = sys.argv[1]

def parseMyFile(file):
  fileData = open(file, "r")
  lines = fileData.readlines()
  
  entries = []
  for line in lines:
    output = line.replace("\n", "").split(" | ")
    entries.append({
      'patterns': output[0].split(" "),
      'signal': output[1].split(" ")})
      
  return entries

########
#.1111.#
#2....3# 
#2....3# 
#.4444.# 
#5....6# 
#5....6#
#.7777.#
########  
# 1: t
# 2: ul
# 3: ur
# 4: m
# 5: bl
# 6: br
# 7: b

def decode(patterns):
  segments = {'ul': '',
          't': '',
          'ur': '',
          'm': '',
          'bl': '',
          'br': '',
          'b': ''}
  charLibrary = "abcdefg"
  
  charSignals = {}
  #use the 2 digit and 3 digit to determine t
  twoChar = filter(lambda length: len(length) == 2, patterns)[0]
  threeChar = filter(lambda length: len(length) == 3, patterns)[0]
  t = None
  
  while(segments['t'] == ''):
    for c in threeChar:
      if c not in twoChar:
        segments['t'] = c
        charLibrary = charLibrary.replace(c, "")
        break
      
  #use the 3 overlapping chars in the 5-char to find middle column
  fiveChars = filter(lambda length: len(length) == 5, patterns)
  middleColumn = []
  while(len(middleColumn) < 3):
    for c in fiveChars[0]:
      if c in fiveChars[1] and c in fiveChars[2]:
        middleColumn.append(c)
  
  #the overlapping character from above that overlaps with the 4-char is m
  fourChar = filter(lambda length: len(length) == 4, patterns)[0]
  for c in middleColumn:
    if c in fourChar:
      segments['m'] = c
      charLibrary = charLibrary.replace(c, "")
    elif c not in threeChar:
      segments['b'] = c
      charLibrary = charLibrary.replace(c, "")
  
  #remaining char NOT in 2-char in 4-char is ul
  for c in fourChar:
    if c not in twoChar and c not in middleColumn:
      segments['ul'] = c
      charLibrary = charLibrary.replace(c, "")
    
  #5-char containing ul is '5' symbol
  for fiveChar in fiveChars:
    if segments['ul'] in fiveChar:
      charSignals['5'] = fiveChar
      
  #2-digit char NOT in 5 is ur, 2-digit char IN 5 is tr
  for c in twoChar:
    if c not in charSignals['5']:
      segments['ur'] = c
      charLibrary = charLibrary.replace(c, "")
    else:
      segments['br'] = c
      charLibrary = charLibrary.replace(c, "")
      
  segments['bl'] = charLibrary[0]

  return segments #(segments, charSignals, charLibrary)
  
def generateCodes(segments):
  codes = {}
  codes['0'] = {segments['ul'], segments['t'], segments['ur'], segments['br'], segments['b'], segments['bl']}
  codes['1'] = {segments['ur'], segments['br']}
  codes['2'] = {segments['t'], segments['ur'], segments['m'], segments['bl'], segments['b']}
  codes['3'] = {segments['t'], segments['br'], segments['ur'], segments['m'], segments['b']}
  codes['4'] = {segments['ul'], segments['m'], segments['ur'], segments['br']}
  codes['5'] = {segments['t'], segments['br'], segments['ul'], segments['m'], segments['b']}
  codes['6'] = {segments['t'], segments['br'], segments['ul'], segments['bl'], segments['m'], segments['b']}
  codes['7'] = {segments['ur'], segments['br'], segments['t']}
  codes['8'] = {segments['t'], segments['br'], segments['ul'], segments['bl'], segments['m'], segments['b'], segments['ur']}
  codes['9'] = {segments['t'], segments['br'], segments['ul'], segments['ur'], segments['m'], segments['b']}


  return codes  
  
  
signals = parseMyFile(fileName)
sum = 0

for signal in signals:
  segments = decode(signal['patterns'])
  codes = generateCodes(segments)
  value = ""
  for chunk in signal['signal']:
    for key in codes:
      # print("Is " + str(set([c for c in chunk])) + " in " + str(codes[key]))
      if set([c for c in chunk]) == codes[key]:
        value += key
        break
  print(value)
  sum += int(value)
  
print(sum)
