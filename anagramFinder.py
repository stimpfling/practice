#!/usr/bin/python

def agFinder(string):
    i = 0
    longestLength = 0
    longestAnagram = "" 
    while i <= len(string)-1:
        j = len(string) 
        while j >= i: 
            print "looking at " + string[i:j] +" where i = " +str(i)+"and j = "+str(j)
            if isAnag(string[i:j]) and j-i+1 > longestLength:
                longestAnagram = string[i:j] 
                longestLength = j-i+1
            if longestLength >= len(string)-i-1:
                return longestAnagram 
            j-=1
        i+=1
    return longestAnagram

def isAnag(string):
    if len(string) == 1:
        return True
    i = 0
    while i < len(string)-1/2:
        if string[i] != string[len(string)-i-1]: 
            return False
        i+=1
    return True

print agFinder("a")
