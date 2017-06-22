#!/usr/bin/python

def plusMinus(n,arr):
    if n == 0:
        return
    posInts = 0
    negInts = 0
    zeroes  = 0 
    for i in arr: 
        if i > 0:
            posInts += 1
        elif i < 0:
            negInts += 1 
        else:
            zeroes += 1
    percentPos = float(posInts/n)
    print str(percentPos) +  " " + str(negInts) + " "+ str(zeroes)
n = 6
arr = [-4,3,-9,0,4,1]
#plusMinus(n,arr)
myNum = float(1)/float(2)
print myNum 

