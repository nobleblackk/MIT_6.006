#!/usr/bin/env python
# coding: utf-8

# #Implementation of Selection-Sort (O(n^2))

# In[1]:


#!/usr/bin/python36

import os 
import subprocess as sp
import math
from random import randint, randrange
import string
from collections import Counter
from heapq import heapify, heappush, heappop
from bisect import bisect, bisect_left, bisect_right
from itertools import permutations, combinations, combinations_with_replacement


# In[2]:


#Complexity => O(n^2)
def selectionSort(arr):
    for i in range(len(arr)):
        min_index = i
        for j in range(i+1, len(arr)):
            if arr[min_index] > arr[j]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index],arr[i]
    return arr


# In[3]:


print(selectionSort([3,4,2,1,0]))


# In[ ]:


###Contributed by NobleBlack

