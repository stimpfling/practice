#!/usr/bin/python
import collections

def findWords(words, matrix): 
    N = len(matrix)
    wordExists = {}
    wordExists = collections.defaultdict(lambda:0,wordExists)

    for word in words: 
        visited = [ [False for x in range(N)] for y in range(N)] 
        startingCoords = findStartingCoords(word, matrix, N)     

        for origin in startingCoords:
            if visitCoord(origin[0],origin[1],visited,matrix,N,word,0):
                wordExists[word] = True 

    for word,exists in wordExists.iteritems():
        if exists: 
            print word + " was found on the board"

def visitCoord(x, y, visited, matrix, N, string, pos):
    if visited[x][y]:
        return
    visited[x][y] = True
    for neighbor in getAllNeighbors(x,y,N):
        if matrix[neighbor[0]][neighbor[1]] == string[pos+1]:
            if pos+1 >= len(string)-1:
                return True
            else:
                return visitCoord(neighbor[0],neighbor[1],visited,matrix,N,string, pos+1)
    return False


def getAllNeighbors(x, y, N):
    neighbors = []
    for i in [x-1, x, x+1]:
        for j in [y-1, y+1]:
            if 0 <= i < N and 0 <= j < N:
                neighbors.append([i,j])
    for j in [y-1, y, y+1]:
        for i in [x-1,x+1]:
            if  0 <= i < N and 0 <= j < N and [i,j] not in neighbors:
                neighbors.append([i,j])
    return neighbors

def findStartingCoords(word, matrix, N):
    if not word:
        return [] 

    results = []
    startingChar = word[0]

    for x in range(N):
        for y in range(N):
            if matrix[x][y] == startingChar:
                results.append([x,y])
    return results



words = ['geeks', "for", "quiz", "go"]
board = [['g', 'i', 'z'],
         ['u', 'e', 'k'],
         ['q', 's', 'e']]
"""
words = ["ABCECF"]
board = [['Z', 'E', 'C'],
         ['F', 'C', 'B'],
         ['Z', 'B', 'A']]
"""
findWords(words, board)


