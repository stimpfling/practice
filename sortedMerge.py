#!/usr/bin/python

def sortMerged(A, B, lenA):
    lastElement = lenA + len(B) - 1
    i = lenA - 1
    j = len(B) - 1
    currElement = lastElement
    while i >= 0 and j >= 0:
        if A[i] >= B[j]:
           A[currElement] = A[i]
           i -= 1
        else:
           A[currElement] = B[j]
           j -= 1
        currElement -= 1
    #todo: if one array is finished, populate the rest of A with the contents of the other.
A = [3,4,6,8,0,0]
B = [1,9]
lenA = 4 
sortMerged(A,B,lenA)
print A
