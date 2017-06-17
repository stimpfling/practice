#!/usr/bin/python

import collections
import sys

class Node:
    def __init__(self, value, left, right):
        self.value = value
        self.left  = left
        self.right = right
    def children(self):
        children = [ self.left, self.right ]
        return children
    
class Tree:
    def __init__(self):
        self.headSet = False
        self.head = None 

    def insertNode(self,node): 
        if not self.headSet:
            self.headSet = True
            self.head = node
            return

        self.__insertNodeRec(node, self.head)

    def __insertNodeRec(self, node, startNode):
        if node.value <= startNode.value:
            if not startNode.left:
                #print "insert " + str(node.value) + " at " + str(startNode.value) + " left"
                startNode.left = node
                return
            else:
                self.__insertNodeRec(node,startNode.left)
        else:
            if not startNode.right:
                startNode.right = node
                return
            else:
                self.__insertNodeRec(node,startNode.right)

    def insertValue(self, value):
        newNode = Node(value, None, None)
        self.insertNode(newNode)

    def insertValueList(self,values):
        for value in values:
            self.insertValue(value)

    def printTreeSimple(self):
        queue = collections.deque()
        queue.appendleft(self.head) 
        while queue: 
            currNode = queue.pop()
            print currNode.value
            for child in currNode.children():
                if child != None: 
                    queue.append(child) 

    def printTreeNicer(self):
        allChildren = []
        currentSet = [self.head]
        while currentSet:
            currentVals = []
            allChildren = []
            for node in currentSet:
                sys.stdout.write(str(node.value))  
                sys.stdout.write(" ")
                for child in node.children():
                    if child != None:
                        allChildren.append(child)
            print
            currentSet = allChildren

mainTree = Tree()
mainTree.insertValueList([4,2,10,1,3,9,11])
head = mainTree.head
mainTree.printTreeSimple()
print
mainTree.printTreeNicer()
