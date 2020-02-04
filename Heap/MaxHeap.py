#!/usr/bin/env python
# coding: utf-8

# #Implementation of Heap-Abstract Data Structure

#!/usr/bin/python36

import os
import subprocess as sp
from random import randint
from bisect import bisect, bisect_left, bisect_right
from heapq import heappush, heappop, heapify
from collections import Counter
import math




class HeapMax:
    HeapSize=10
    def __init__(self):
        self.heap=[0]*(HeapMax.HeapSize)
        self.currentPosition=-1
    def insertion(self,data):
        if self.isFull():
            print("Heap is full")
            return
        else:
            self.currentPosition+=1
            self.heap[self.currentPosition]=data
            self.heapify(self.currentPosition)
    def isFull(self):
        if self.currentPosition==(HeapMax.HeapSize)-1:
            return True
        else:
            return False
    def heapify(self,index):
        parentIndex=(index-1)//2
        while parentIndex>=0 and self.heap[parentIndex]<self.heap[index]:
            self.heap[parentIndex],self.heap[index]=self.heap[index],self.heap[parentIndex]
            index=parentIndex
            parentIndex=(index-1)//2
    def heapSort(self):
        print("HeapSort:")
        for i in range(0,self.currentPosition+1,1):
            temp=self.heap[0]
            print(temp,end=' ')
            self.heap[0]=self.heap[self.currentPosition-i]
            self.heap[self.currentPosition-i]=temp# =>Useless, bcoz we gonna drop this anyway
            self.fixDown(0,self.currentPosition-i-1)
        print()
        print(self.heap)
        self.buildHeap()
        print(self.heap)
    def buildHeap(self):
        n=(self.currentPosition-1)//2
        for i in range(n,-1,-1):
            self.fixDown(i,self.currentPosition)
    def fixDown(self,index,upto):
        while index<upto:
            leftChild=(index*2)+1
            rightChild=(index*2)+2
            if leftChild <= upto:
                childToSwap=None
                if rightChild>upto:
                    childToSwap=leftChild
                else:
                    if self.heap[leftChild]>self.heap[rightChild]:
                        childToSwap=leftChild
                    else:
                        childToSwap=rightChild
                if self.heap[index]<self.heap[childToSwap]:
                    self.heap[index],self.heap[childToSwap]=self.heap[childToSwap],self.heap[index]
                    index=childToSwap
                else:
                    break
            else:
                break
                    
    def printHeap(self):
        print("Representation of MaxHeap in Array-Form:")
        for i in range(0,self.currentPosition+1):
            print(self.heap[i],end=' ')
        print()
    
            


a=HeapMax()
a.insertion(16)
a.insertion(4)
a.insertion(10)
a.insertion(14)
a.insertion(7)
a.insertion(9)
a.insertion(3)
a.insertion(2)
a.insertion(8)
a.insertion(1)
a.printHeap()
a.heapSort()


					###Contributed by NobleBlack




