#!/usr/bin/python
def getAnagramIndices(haystack, needle):
# write your code here
    indicies=[]
    window = len(needle)
    for i,val in enumerate(haystack):
        if i+window > len(haystack):
            return indicies
        if isInWindow(haystack[i:i+window],needle):
            indicies.append(i)
    return indicies

def isInWindow(haystack,needle):
    charDict = {}
    for char in haystack:
        if char in charDict:
            charDict[char] +=1
        else:
            charDict[char] = 1
    for char in needle:
        if char in charDict:
            if charDict[char] >=1:
                charDict[char] -=1
            else:
                return False
        else:
            return False
    return True

haystack1 = "aaaa" 
needle1 = "aa"
print getAnagramIndices(haystack1,needle1)
