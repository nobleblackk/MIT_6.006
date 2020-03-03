#!/usr/bin/env python
# coding: utf-8

# #Implementation of Rat in a Maze

# In[ ]:


#!/usr/bin/python36

import os 
import subprocess as sp
import math
from random import randint, randrange
from itertools import permutations, combinations, combinations_with_replacement
from collections import Counter, deque
from heapq import heapify, heappush, heappop
from string import ascii_letters, ascii_lowercase, ascii_uppercase
from bisect import bisect, bisect_left, bisect_right


# In[11]:


class Maze:
    def __init__(self,N):
        self.N = N
        self.maze = [[] for i in range(self.N)]
        self.ratPath = [[0 for i in range(self.N)] for j in range(self.N)]
    def inputGrid(self):
        print("Please Input The Grids for " + str(self.N) + "Grid Numbers::" )
        for i in range(self.N):
            self.maze[i] = list(map(int,input().split()))
    def isPossible(self,x,y):
        if ((x >= 0 and x < self.N) and (y >= 0 and y < self.N) and self.maze[x][y] == 0):
            return True
        return False
    def mazeSolution(self,x,y):
        if x == self.N - 1 and y == self.N - 1:
            self.ratPath[x][y] = 1
            return True
        if (self.isPossible(x,y)):
            self.ratPath[x][y] = 1
            if (self.mazeSolution(x+1,y)):
                return True
            if (self.mazeSolution(x,y+1)):
                return True
        return False
    def rat(self):
        if (self.mazeSolution(0,0) == True):
            for i in range(self.N):
                for j in range(self.N):
                    print(self.ratPath[i][j], end = ' ')
                print()
        else:
            print("Solution Not Possible")


# In[15]:


maze = Maze(4)


# In[18]:


maze.inputGrid()


# In[19]:


maze.rat()


# In[ ]:


###Contributed By NobleBlack

