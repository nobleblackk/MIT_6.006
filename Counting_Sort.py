#!/usr/bin/env python
# coding: utf-8

# #Implementation of Counting-Sort

# In[1]:


#!/usr/bin/python36

import os
import subprocess as sp
from bisect import bisect, bisect_left, bisect_right
from random import randint
from collections import Counter
import math
from heapq import heappush, heappop, heapify


# In[21]:


def array1D(n):
    arr=[]
    for i in range(n):
        arr.append(randint(1,10))
    print(arr)
    return arr


# In[22]:


def countingSort(arr): #O(n+k)
    k = max(arr) #O(len(arr))
    aux = [0]*(k+1) #O(k)
    print(aux)
    
    for i in range(len(arr)): #O(len(arr))
        aux[arr[i]]+=1
        print(aux)
    
    ans=[]
    j=0
    for i in range(k+1):
        temp=aux[i]
        while temp:
            ans.append(i)
            temp-=1
    return ans


# In[23]:


###Driver-Code
n=int(input("Input no of Elements"))
arr=array1D(n)
print(countingSort(arr))
                    ###Contributed by NobleBlack


# In[ ]:




