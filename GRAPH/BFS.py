#!/usr/bin/env python
# coding: utf-8

# Implementation of BFS(Breadth First Search)
# 
# 

# In[1]:


#!/usr/bin/python36

import os
import subprocess as sp
import math
from random import randint, randrange
from string import ascii_letters, ascii_lowercase, ascii_uppercase
from collections import Counter
from itertools import permutations, combinations, combinations_with_replacement
from bisect import bisect, bisect_left, bisect_right
from heapq import heapify, heappush, heappop
from decimal import Decimal


# In[2]:


class Node:
    def __init__(self, vertex):
        self.vertex = vertex
        self.adjacencyList = []
        self.predecessor = None
        


# In[3]:


class BFS:
    def bfs(self,startNode):
        level = {startNode : 0}
        parent = {startNode : None}
        frontier = [startNode]
        
        startNode.predecessor = parent[startNode]
        i = 1
        print(startNode.vertex)
        while frontier:
            next = []
            for vertex in frontier:
                    for neighbours in vertex.adjacencyList:
                        if neighbours not in level:
                            print(neighbours.vertex)
                            level[neighbours] = i
                            parent[neighbours] = vertex
                            neighbours.predecessor = parent[neighbours]
                            next.append(neighbours)
            frontier = next
            i += 1
            
        


# In[5]:


a = Node('a')
b = Node('b')
c = Node('c')


abc = BFS()

a.adjacencyList.append(b)
a.adjacencyList.append(c)

abc.bfs(a)


# In[ ]:


###Contributed by NobleBlack

