#!/usr/bin/env python
# coding: utf-8

# #Implementation of Counting-Sort

# In[5]:


#!/usr/bin/python3

import os 
import subprocess as sp
import math
from random import randint 
from collections import Counter
from bisect import bisect, bisect_left, bisect_right
from heapq import heappush, heappop, heapify


# In[13]:


def array1D(n):
    arr=[]
    for i in range(n):
        arr.append(randint(1,10))
    print(arr)
    return arr


# In[22]:


def countingSort(arr):
    Max=max(arr) #finding the maximum value
    count=[0]*(Max+1) #making array as the length of largest element present
    for i in range(len(arr)): #storing count of each element present in array
        count[arr[i]]+=1
    print(count)
    
    for i in range(1,Max+1): #storing the actual positon of elements of the array in count array
        count[i]+=count[i-1]
    print("with position",count)
    
    res=[0]*len(arr)
    i=len(arr)-1
    while i>=0: #"res" array with the right order 
        res[count[arr[i]]-1]=arr[i]
        count[arr[i]]-=1
        i-=1
    return res
        
    
    


# In[23]:


###Driver-Code
n=int(input("input no"))
arr=array1D(n)
print(countingSort(arr))


					###Contributed by NobleBlack




