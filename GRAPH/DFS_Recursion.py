#!/usr/bin/env python
# coding: utf-8

# #Implementation of DFS(Depth First Search) using Recursion

# In[1]:


#!/usr/bin/python36

import os
import subprocess as sp
import math
from random import randint, randrange
from string import ascii_letters, ascii_lowercase, ascii_uppercase
from collections import Counter
from heapq import heapify, heappush, heappop
from itertools import permutations, combinations, combinations_with_replacement
from bisect import bisect, bisect_left, bisect_right


# In[2]:


class Node:
    def __init__(self,vertex):
        self.vertex = vertex
        self.visited = False
        self.adjacencyList = []
        


# In[6]:


class DFS:
    def dfs(self,s):
        s.visited = True
        print(s.vertex)
        for neighbour in s.adjacencyList:
            if neighbour.visited != True:
                self.dfs(neighbour)


# In[7]:


demo = DFS()
a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)
a.adjacencyList.append(b)
a.adjacencyList.append(d)
b.adjacencyList.append(a)
b.adjacencyList.append(c)
b.adjacencyList.append(d)
demo.dfs(a)


# In[ ]:


###Contributed by NobleBlack

