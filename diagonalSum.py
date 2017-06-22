#!/usr/bin/python

def diagonalSum(dimension,array):
    i = 0 
    j = dimension - 1
    firstSum = 0
    secondSum = 0
    while i < dimension:
        print "adding " + str(array[i][i]) + " and " + str(array[i][j]) 
        firstSum += array[i][i]
        secondSum += array[i][j]
        i+=1
        j-=1
    total = firstSum - secondSum
    print abs(total) 

a = [[11,2,4],[4,5,6],[10,8,-12]]
diagonalSum(3,a)
