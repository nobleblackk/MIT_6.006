#!/usr/bin/env python
# coding: utf-8

# #Implementation of Bubble-Sort (O(n^2))

# In[1]:


#!/usr/bin/python36

import os
import subprocess as sp
import math
from random import randint, randrange
from collections import Counter
from bisect import bisect, bisect_left, bisect_right
import string
from heapq import heapify, heappush, heappop
from itertools import permutations, combinations ,combinations_with_replacement


# In[2]:


#Complexity => (O(n^2))
def bubbleSort(arr):
    for i in range(len(arr)):
        for j in range(0,len(arr)-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1],arr[j]
    return arr

        


# In[3]:


print(bubbleSort([3,4,2,1]))


# In[ ]:


###Contributed by NobleBlack

