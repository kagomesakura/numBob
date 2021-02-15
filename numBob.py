#print how many times the word bob occurs in string

s = 'azcbobobegghakl'
numBob = 0

for i in range(len(s)):
    if s[i:i+3] == "bob":
        #The reason this works is that range returns a list of numbers
        #in order, so it will go 0, 1, 2, 3... the [i:i+3]
        #part cuts out a section of the string based on the how far into the string it is.
        numBob += 1

print ('Number of times bob occurs is: ' + str(numBob))
