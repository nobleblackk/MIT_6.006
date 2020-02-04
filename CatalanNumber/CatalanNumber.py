#!/usr/bin/env python
# coding: utf-8

# #Implementation of Catalan-Number

# In[2]:


import os 
import subprocess as sp
import math
from random import randint, randrange
import string
import collections
from bisect import bisect, bisect_left, bisect_right
from heapq import heapify, heappush, heappop


# In[3]:


class Catalan:
    def catalan(self,num):
        if num <= 1:
            return 1
        temp = 0
        for i in range(num):
            temp += (self.catalan(i)*self.catalan(num-i-1))
            #print(self.count)
        return temp


# In[ ]:


demo = Catalan()
a = demo.catalan(100)
a


# In[ ]:


###Contributed by NobleBlack 


# In[ ]:




