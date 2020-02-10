#!/usr/bin/env python
# coding: utf-8

# #Implementation of Doubly-LinkedList 

# In[ ]:


#!/usr/bin/python36

import os 
import subprocess as sp
import math
from random import randint, randrange
from string import ascii_letters, ascii_lowercase, ascii_uppercase
from itertools import combinations, combinations_with_replacement, permutations
from bisect import bisect, bisect_left, bisect_right
from collections import Counter
from heapq import heapify, heappush, heappop


# In[4]:


class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.previous = None


# In[49]:


class DLL:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def insertionStart(self,data):
        ###When LL is Empty 
        if self.head == None:
            self.head = Node(data)
            self.tail = self.head
        else:
            temp = Node(data)
            temp.next = self.head
            (self.head).previous = temp
            self.head = temp
    
    def insertionEnd(self,data):
        ###when LL is Empty
        if self.head == None:
            self.head = Node(data)
            self.tail = self.head
        else:
            temp = Node(data)
            self.tail.next = temp
            temp.previous = self.tail
            self.tail = temp
            
    def deletion(self,data):
        ###when LL is Empty
        if self.head == None:
            print("LinkedList is Empty")
            return
        elif self.tail.data == data:
            self.tail.previous.next = None
            return
        previous = None
        current = self.head
        while current.data != data:
            previous = current 
            current = current.next
        if previous == None:
            self.head = current.next
            self.head.previous = None
        else:
            previous.next = current.next
            (current.next).previous = previous
    
    def printLL(self):
        if self.head == None:
            print("LinkedList is Empty")
            return
        else:
            cur = self.head
            while cur != None:
                print(cur.data)
                cur = cur.next
            
            


# In[52]:


demo = DLL()
demo.insertionStart(4)
demo.insertionStart(3)
demo.insertionStart(2)
demo.insertionStart(1)
demo.insertionEnd(5)
demo.insertionEnd(6)
demo.insertionEnd(7)
demo.insertionEnd(8)
demo.printLL()
demo.deletion(4)
print("new")
demo.printLL()


# In[ ]:


###Contributed by NobleBlack


# In[ ]:




