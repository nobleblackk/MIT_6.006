#!/usr/bin/env python
# coding: utf-8

# #Implementation of Quick-Sort (Avg Case => O(nlogn)) 

# In[1]:


#!/usr/bin/python36

import os
import subprocess as sp
import math
import string
from random import randint, randrange
from heapq import heapify, heappop, heappush
from itertools import permutations, combinations, combinations_with_replacement
from bisect import bisect, bisect_left, bisect_right
from collections import Counter


# In[15]:


def partition(arr,start,end):
    pivot = arr[end]
    i = start - 1
    for j in range(start,end):
        if arr[j] < pivot:
            i += 1
            arr[i],arr[j] = arr[j],arr[i]
    i += 1
    arr[i],arr[end] = arr[end],arr[i]
    return i
    
def quickSort(arr,start,end):
    if start < end:
        pivot_index = partition(arr,start,end)
        #print(pivot_index)
        quickSort(arr,start,pivot_index-1)
        quickSort(arr,pivot_index+1,end)
    return arr ; 


# In[16]:


print(quickSort([4,3,2,1],0,3))


# In[ ]:


###Contributed by NobleBlack

