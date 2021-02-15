#print how many times the word bob occurs in string

s = 'azcbobobegghakl'
numBob = 0

for i in range(len(s)):
    if s[i:i+3] == "bob":
        # [i:i+3] checks the current char + the next three chars.
        numBob += 1

print ('Number of times bob occurs is: ' + str(numBob))
