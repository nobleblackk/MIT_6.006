#!/usr/bin/env python
# coding: utf-8

# #Implementation of DFS(Depth First Search) using Stack

# In[1]:


#!/usr/bin/python36

import os
import subprocess as sp
import math
from random import randint, randrange
from string import ascii_letters, ascii_lowercase, ascii_uppercase
from heapq import heapify, heappush, heappop
from collections import Counter
from bisect import bisect, bisect_left, bisect_right
from itertools import permutations, combinations, combinations_with_replacement


# In[2]:


class Node:
    def __init__(self,vertex):
        self.vertex = vertex
        self.visited = False
        self.adjacencyList = [] 


# In[3]:


###DFS using Iteration(Stack)
class DFS:
    def dfs(self,s):
        frontier = [s]
        while frontier:
            vertex = frontier.pop()
            print(vertex.vertex)
            vertex.visited = True
            for neighbours in vertex.adjacencyList:
                if neighbours.visited != True:
                    frontier.append(neighbours)
                    


# In[5]:


demo = DFS()
a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)
a.adjacencyList.append(b)
a.adjacencyList.append(c)
c.adjacencyList.append(d)
b.adjacencyList.append(c)
b.adjacencyList.append(d)
demo.dfs(a)


# In[ ]:


###Contributed by NobleBlack 

