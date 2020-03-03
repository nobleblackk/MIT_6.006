#!/usr/bin/env python
# coding: utf-8

# #Implementation of PowerSet Using Iteration

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


# In[7]:


def powerSet(arr):
    for i in range(0,2**len(arr)):
        count = "" 
        for j in range(0,len(arr)):
            if (i & (1 << j)) :
                count += arr[j]
        print(count, end = ", ")
powerSet("abc")
        


# In[ ]:


###Contributed by NobleBlack

