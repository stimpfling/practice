#!/usr/bin/python
import copy
def rotate(matrix):
    x = y = 0
    N = len(matrix)-1
    length = len(matrix)
    replica = copy.deepcopy(matrix)
    
    while x < length/2:
        y = 0
        while y < length:
            print "replica " + str(y),str(N-x)+" = " + str(x),str(y)
            matrix[x][y] = tmp2 
            matrix[y][N-x] = matrix[x][y]
            y+=1
        x+=1
    return replica

matrix = [[1,2],[3,4]]
#matrix[0][0] = 1 
print rotate(matrix)

