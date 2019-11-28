#!/usr/bin/env python
# coding: utf-8

# #Implementation of Radix-Sort

# In[1]:


#!/usr/bin/python3

import os 
import subprocess as sp
import math
from random import randint 
from collections import Counter
from bisect import bisect, bisect_left, bisect_right
from heapq import heappush, heappop, heapify


# In[6]:


def array1D(n):
    arr=[]
    for i in range(n):
        arr.append(randint(1,10))
    print(arr)
    return arr


# In[13]:


def radixSort(arr): #We are assuming that numbers are always decimals. So base=>10 :)
    Max=max(arr)
    exp=1
    while (Max//exp) > 0: #O(d(n+b)) ,  
        arr = countingSort(arr,exp)
        exp*=10
    return arr
    
    ###feasible -> Max<=polynomial of n but not n^n
    ###d(n+b) -> logb(k)(n+b) -> when k => polynomail in n i.e. n^1,n^2,n^3,n^4...n^n-1
    ###what 'b' we want, lets say , if b is o(n), then ->
    ###logn(k)(n+o(n))=>logn(k)(n) and now, -> what 'k' we want, lets say,
    ###k should be polynomail of 'n' but not 'n^n' so when it is polynomail in n, then ->
    ###logn(n^c)(n) => c(logn(n))(n) => c((1)n) => so it is linear
    ###where c is any arbitary number
    
    


# In[17]:


def countingSort(arr,exp):
    b=[0]*10 #as only decimals are coming this way
    
    
    for i in range(len(arr)): #Keeping the count of numbers, their digit-wise.
        b[(arr[i]//exp)%10]+=1
    
    for i in range(1,len(b)): #updating the indices with actual positions (O(b))
        b[i]+=b[i-1]
    res=[0]*len(arr)
    i=len(arr)-1
    while i>=0: #O(n)
        res[b[(arr[i]//exp)%10]-1]=arr[i]
        b[(arr[i]//exp)%10]-=1
        i-=1
    return res
        




n=int(input("enter value"))
arr=array1D(n)





arr=radixSort(arr)
print(arr)


					###Contributed by NobleBlack



