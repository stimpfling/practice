#!/usr/bin/python

def findBlackPixels(array, x, y):



def visitNode(array, x, y, visitedNodes, blackPixels):
    if visitedNodes[x][y] == 1 or array[x][y] == 0: 
        visitedNodes[x][y] = 1
        return
    visitedNodes[x][y] = 1

    for i in [x+1,x-1]:
        for j in [y+1,y-1]:
            visitNode(array,i,j,visitedNodes,blackPixels)
    

