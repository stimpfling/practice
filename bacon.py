#!/usr/bin/python
import collections

class Movie:
    def __init__(self,movie,actors):
        self.actors = actors
        self.name = movie

class ActorGraph:
    def __init__(self):
        self.graph = collections.defaultdict(set)

    def addMovie(self,Movie):
        for actor in Movie.actors:
            for person in Movie.actors:
                self.graph[actor].add(person) 

mainGraph = ActorGraph()
mainGraph.addMovie(Movie("Two Brothers",["Alice","Bob","Jimmy","Yakov"]))
mainGraph.addMovie(Movie("One Brother",["Bob","Jimmy"]))
mainGraph.addMovie(Movie("It Happened",["Alice","Scooter"]))
mainGraph.addMovie(Movie("It Happened Again",["Gunter","Scooter"]))
mainGraph.addMovie(Movie("Night Dogs",["Gunter","Harry"]))


def baconDegree(actor1, actor2, graph):
    distances = {}
    nodeList = {}
    for actor in graph:
        distances[actor] = float("inf")
    distances[actor1] = 0

    shortestPath(actor1, actor2, graph, distances, nodeList)
    print actor1 + " is " + str(distances[actor2]) + " degrees away from " + actor2
    print "Path: " 
    path = actor2
    while(path != actor1):
        print path
        path = nodeList[path] 
    return

def shortestPath(actor1, actor2, graph, distances, nodeList):
    actor = actor1
    queue = collections.deque([actor1])
    visited = {} 
    while queue: 
        actor = queue.popleft()
        visited[actor] = True
        for child in graph[actor]:
            if distances[actor]+1 < distances[child]:
                distances[child] = distances[actor]+1
                nodeList[child] = actor
            if child not in visited:
                queue.append(child)
    return 

baconDegree("Harry","Alice",mainGraph.graph)


