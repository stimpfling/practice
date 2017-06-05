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
    if minPos == 0 and maxPos == len(arr)-1:
        order = "asc" 
    elif minPos == len(arr) - 1 and maxPos == 0:
        order = "desc"
    elif minPos < maxPos: 
        order = "desc circ"
    else:
        order = "asc circ"
    print str(maxVal) + " "+ order 

#asc
whatOrder([0,1,2,3,4])
#desc
whatOrder([4,3,2,1,0])
#desc circ
whatOrder([0,4,3,2,1])
whatOrder([3,2,1,0,4])
whatOrder([2,1,0,3,4])
#asc circ
whatOrder([1,2,3,4,0])
whatOrder([4,0,1,2,3])
whatOrder([3,4,0,1,2])
