#!/usr/bin/python
def longestPal(string):
    longestSoFar = 0
    longestPal = ""
    for i,val in enumerate(string): 
        if val in string[i+1:]:
            endIndex = string[i+1:].index(val)
            endIndex = endIndex + i + 2
            print "Testing string["+str(i)+":"+str(endIndex)+"] =" + string[i:endIndex]
            if endIndex - i > longestSoFar and isPal(string[i:endIndex]):
                longestSoFar = endIndex - i 
                longestPal = string[i:endIndex]
        else:
            next
    return longestPal

def isPal(string):
    end = len(string)-1
    i = 0
    while i <= end:
        if string[i] != string[end]:
            return False
        i+=1
        end-=1
    return True

print isPal("abbaabba")
print longestPal("abcdefg")
#print string[1:].index("g")
#string = "abcdefg"
#print string[1:]
