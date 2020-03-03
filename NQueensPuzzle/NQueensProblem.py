#!/usr/bin/env python
# coding: utf-8

# #Implementation of NQueens Problem

# In[1]:


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


# In[14]:


class Board:
    def __init__(self,n):
        self.N = n
        self.board = [[0 for i in range(self.N)] for j in range(self.N)]
    
    def isSafe(self,row,column):
        #checking for same row but previous columns for collisions
        i = 0; 
        while i < column:
            if self.board[row][i] == 1:
                return False
            i += 1
        
        #checking for left upper diagonal elements for collisions
        i = row - 1; j = column - 1
        while (i >= 0 and j >= 0):
            if self.board[i][j] == 1:
                return False
            i -= 1; j -= 1
        
        #checking for left lower diagonal elements for collisions
        i = row + 1; j = column - 1
        while (i < self.N and j >= 0):
            if self.board[i][j] == 1:
                return False
            i += 1; j -= 1
        #It means, our queen is good to be placed at this position,
        #no collisions found
        return True
    
        
        
        
    def nQueensProblem(self,column):
        if column == self.N:
            return True
        #Going to check for each row to place queen without violation 
        for row in range(0,self.N):
            #to check whether it doesn't violate to any earlier queen position
            if (self.isSafe(row,column) == True): #means, we can place our queen here :)
                self.board[row][column] = 1
                #Checking for next positions, as all earlier queens are satisfied
                if (self.nQueensProblem(column + 1) == True):
                    return True
                #it means, further position is creating collision with earlier queen placed,
                #so , we would search for other position and make it zero
                self.board[row][column] = 0
        return False
    
    #Driver code to Execute N-Queens Problem
    def queen(self):
        if self.nQueensProblem(0) == True:
            for i in range(self.N):
                for j in range(self.N):
                    print(self.board[i][j],end = ' ')
                print()
        else:
            print("Solution Not Possible")
    
    
    
                


# In[21]:


board= Board(4)
board.queen()


# In[ ]:





# In[ ]:




