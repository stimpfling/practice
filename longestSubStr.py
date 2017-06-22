#!/usr/bin/python

def longestSubStr(string):
    longestLen = 0
    currentLen = 0
    longestStr = ""
    subStr = "";
    for char in string:
        if char not in subStr: 
            subStr = subStr + char  
            currentLen += 1
            print "substr = " + subStr
            if currentLen >= longestLen:
                longestLen = currentLen 
                print "Longest len = " + str(longestLen)
                longestStr = subStr
        else: 
            i = 0
            while i < len(subStr):
                if subStr[i] == char:
                    subStr = subStr[i+1:] + char 
                    break
                i+=1
            print "new substr = " + subStr
            currentLen = len(subStr)
    return longestStr
            

print longestSubStr("dvdf")

