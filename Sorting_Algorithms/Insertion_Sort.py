#!/usr/bin/env python
# coding: utf-8

# Implementation of Insertion Sort.
# Contributed by NobleBlack.




#!/usr/bin/python36
import os 
import subprocess as sp
from random import randint




def Array1D(n):
    arr=[]
    for i in range(n):
        arr.append(randint(1,100))
    return arr




def Insertion_Sort(A):
    for i in range(1,len(A),1):
        if A[i]<A[i-1]:
            A[i],A[i-1]=A[i-1],A[i]
            for j in range(i,0,-1):
                if A[j]<A[j-1]:
                    A[j],A[j-1]=A[j-1],A[j]
    print(A)        

Insertion_Sort([5,2,4,-6,1,3])




#Driver Code
n=int(input("Input Size of Array"))
arr=Array1D(n)
print("Array is:",arr)
print("Sorted Array is:",end='')
Insertion_Sort(arr)
                    ###Contributed by NobleBlack






