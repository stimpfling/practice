#!/usr/bin/python

def whatOrder(arr): 
    minVal = arr[0]
    maxVal = arr[0]
    minPos = 0
    maxPos = 0
    for i,val in enumerate(arr): 
        if val > maxVal: 
            maxVal = val
            maxPos = i
        if val < minVal:
            minVal = val
            minPos = i 
    if minPos == 0:
        order = "asc" 
    elif minPos == len(arr) - 1:
        order = "desc"
    elif minPos < maxPos: 
        order = "desc circ"
    else:
        order = "asc circ"
    print str(maxVal) + " "+ order 

#asc
whatOrder([0,1,2,3,4,5])
#desc
whatOrder([5,4,3,2,1,0])
#desc circ
whatOrder([3,2,1,0,5,4])
#asc circ
whatOrder([3,4,5,0,1,2])
