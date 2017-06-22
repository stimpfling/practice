#!/usr/bin/python

def getPixelGroups(img, size):
    visited =[[0 for x in range(size)] for y in range(size)] 
    all_groups = []    
    for x in range(size):
        for y in range (size):
            group = []
            visitPixel(img,x,y,group,visited, size) 
            if group:
                all_groups.append(group)
    return all_groups

def visitPixel(img, x, y, group, visited, size):
    if visited[x][y] or not img[x][y]: 
        visited[x][y] = 1
        return

    visited[x][y] = 1
    group.append([x,y])

    for j in [y-1,y+1]:
        if 0 <= j < size: 
            visitPixel(img, x, j, group, visited, size)
    for i in [x-1,x+1]:
        if 0 <= i < size: 
            visitPixel(img, i, y, group, visited, size)
 

""" Should return [[0,1][1,1][2,1]] 
img1 = [[0,1,0],
        [0,1,0],
        [0,1,0]]
print getPixelGroups(img1,3)
"""

img2 = [[1,0,0],
        [0,0,1],
        [0,0,0]]
for group in getPixelGroups(img2,3):
    print group
