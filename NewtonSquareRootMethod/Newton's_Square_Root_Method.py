#!/usr/bin/env python
# coding: utf-8

# Implementation of Newton's Square Root Method

# In[1]:


#!/use/bin/python36

import os 
import subprocess as sp
import math
from random import randint, randrange
import collections
from bisect import bisect, bisect_left, bisect_right
from decimal import *
from heapq import heapify, heappop, heappush
import string


# In[16]:


"""
Square root of any number upto millions of digits can be calculated using Newton's Method,
it uses Equation of Tangent as [y = f(x) + f'(x).(x-xi)] and then calculate for the root of 
equation through successive approach and after certain repetitions it get the square root.
Equation for Square Root => x(i+1) = (xi + (a/xi))/2
"""
def Newton(number,iterations=500):
    a = float(number)
    for i in range(iterations):
        number = (number + (a/number))/2
    return number

    
        


# In[17]:


print(Newton(2))


# In[ ]:




