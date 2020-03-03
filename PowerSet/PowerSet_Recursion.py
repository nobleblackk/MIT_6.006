#!/usr/bin/env python
# coding: utf-8

# #Implementation of PowerSet using Recursion

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


# In[3]:


def powerSet(arr,index, string):
    if index == len(arr):
        print(string, end = ' ')
        return
    powerSet(arr, index + 1, string)
    powerSet(arr, index + 1, string + arr[index])
powerSet("abc", 0, "")


# In[ ]:


###Contributed By NobleBlack

