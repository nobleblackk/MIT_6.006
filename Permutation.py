#!/usr/bin/env python
# coding: utf-8

# #Implementation of Permutation.
# 

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


# In[4]:


def permute(arr,l,r):
    if l == r:
        print(arr);
    else:
        for i in range(l,r+1):
            arr[l], arr[i] = arr[i], arr[l]
            permute(arr,l+1,r)
            arr[l], arr[i] = arr[i], arr[l]

permute(['a','b','c'],0,2)
    


# In[ ]:


###Contributed by NobleBlack

