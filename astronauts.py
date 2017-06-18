#!/usr/bin/python
import collections

def numCrews(countryList, N):
    relatedList,numUnique = resolveRelated(countryList,N)
    print relatedList,numUnique
    """ Do the math stuff now"""

def resolveRelated(countryList, N):
    adjList = collections.defaultdict(set) 
    numUnique = N
    relatedList = [] 
    visited = collections.defaultdict(lambda:False)
    for a,b in countryList:
        adjList[a].add(b)
        print adjList 

    for start in adjList.keys():
        if not visited[start]:
            numRelated = bfsCount(adjList, relatedList, visited, start)
            relatedList.append(numRelated)
            numUnique -= numRelated
    return relatedList, numUnique

def bfsCount(adjList, relatedList, visited, start):
    queue = collections.deque()
    queue.appendleft(start) 
    currentTotal = 1
    while queue:
        current = queue.pop()
        visited[current] = True
        for child in adjList[current]:
            if not visited[child]:
                queue.appendleft(child)
                currentTotal +=1
    return currentTotal 
     
    
"""
0-1-2-5 
3-4-6

"""
astronauts = [ [0,1], [1,2], [3,4], [1,5], [4,6] ]  
numCrews(astronauts, 10)
