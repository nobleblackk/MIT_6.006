#!/usr/bin/env python
# coding: utf-8

# Implementation of Karastuba Multiplication Mehtod
# 

# In[30]:


#!/usr/bin/python36

import os
import subprocess as sp
import math
import string
from random import randint, randrange
import collections
from bisect import bisect, bisect_left, bisect_right
from heapq import heapify, heappush, heappop


# In[31]:


"""
Kartsuba Multiplication Method is used to perform multiplication for two long digits in 
efficient way, the normal grade school method takes O(n**2) Complexity but Karatsuba 
requires only O(n**log2(3)) ~ O(n**(1.585)) which is quite efficient.
this method can also be used in the situations where there might occur any possibility of 
having the product of multiplication greater than the size of specific word-size(32,64 etc.).
it uses the divide and conquer Paradigm, it makes the two halves of each digit and repeat this
process until we get significantly lower digit(in my case which is 1) then we only perform 
multiplication for 3 pairs and get the result same as done by the process we learnt in grade 
school, 
P.S. Karatsuba used the very famous trick known as Guass's Trick to evaluate multiplication.
"""
class Karatsuba:
    def __init__(self):
        self.product = 0
    def multiplication(self,x,y):
        if len(str(x)) == 1 or len(str(y)) == 1:
            return x*y
        else:
            n = max(len(str(x)), len(str(y))) // 2 

            a = x // (10**n)
            b = x % (10**n)
            c = y // (10**n)
            d = y % (10**n)

            ac = self.multiplication(a,c)
            bd = self.multiplication(b,d)

            ad_bc = self.multiplication(a+b,c+d) - ac - bd

            self.product = (ac*(10**(n*2))) + (ad_bc*(10**n)) + bd 
        return self.product


# In[33]:


demo = Karatsuba()
print(demo.multiplication(12,100))


# In[ ]:


###Contributed by NobleBlack

