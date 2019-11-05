#!/usr/bin/env python
# coding: utf-8

# Implementation of Merge_Sort.


#!/usr/bin/python36
import os
import subprocess as sp
from random import randint 




def merge(arr,start,mid,end):
    temp=[0]*(end-start+1)
    i,j,k=start,mid+1,0
    while i<=mid and j<=end:
        if arr[i]<arr[j]:
            temp[k]=arr[i]
            i+=1
            k+=1
        else:
            temp[k]=arr[j]
            j+=1
            k+=1
    #including the rest elements of i
    while i<=mid:
        temp[k]=arr[i]
        i+=1
        k+=1
    #including the rest elements of j
    while j<=end:
        temp[k]=arr[j]
        j+=1
        k+=1
    for i in range(start,end+1):
        arr[i]=temp[i-start]
        




def mergeSort(arr,start,end):
    mid=start+(end-start)//2
    if start<end:
        mergeSort(arr,start,mid)
        mergeSort(arr,mid+1,end)
        merge(arr,start,mid,end)
    #print(arr)




mergeSort([4,3,2,1],0,3)


					###Contributed by NobleBlack



