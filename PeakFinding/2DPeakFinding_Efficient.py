#!/usr/bin/env python
# coding: utf-8

# In[21]:


from random import randint
#Input for 2DArray using function randint
def Array2D(m,n):
    arr=[[randint(1,1000) for i in range(n)] for j in range(m)]
    return arr
###In this Efficient Method , instead of extracting local peak by traversing all elements,
###We are simply using DNC (Devide and Conquer) approach to find local 1D Peak.
###It will reduce the complexity from O(m) to O(log m)
###Overall Complexity will be O(logmlogn) which is quite good as comparative to prior one
###which were O(m*logn)
def Peak1D(a):
    if a[0] >= a[1]:
        return 0
    elif a[-1] >= a[-2]:
        return len(a)-1
    return FindPeak1D(a,0,len(a)-1)

def FindPeak1D(a,start,end):
    mid = start + (end-start)//2
    if start == end:
        return a.index(a[mid])
    elif a[mid] < a[mid+1]:
        return FindPeak1D(a,mid+1,end)
    elif a[mid] < a[mid-1]:
        return FindPeak1D(a,0,end)
    else:
        return a.index(a[mid])




#Function to extract Global-Maxima for each Column intake
def Maxima(arr,mid):
    a=[row[mid] for row in arr]
    #i=a.index(max(a))
    index=Peak1D(a)
    return index

#Function to fine 2DArray-Peak
def FindPeak2D(arr,m,n):
    if len(arr[0]) == 1:
        return max(arr)
    return Peak2D(arr,0,n-1,m)

#Function for finding 2DPeak using Recursion
def Peak2D(arr,start,end,m): 
    mid=start + (end-start)//2
    print("mid",mid)
    index=Maxima(arr,mid)
    if start == end:
        return arr[index][mid]
    if arr[index][mid] < arr[index][mid+1]:
        return Peak2D(arr,mid+1,end,n)
    elif arr[index][mid] < arr[index][mid-1]:
        return Peak2D(arr,0,mid-1,n)
    else:
        return arr[index][mid]
    


# In[28]:


#Driver-Code for Finding 2DPeak
m,n=map(int,input("Input No of Rows and Columns").split())
arr=Array2D(m,n)
print(arr)
element=FindPeak2D(arr,m,n)
element
                ###Contributed by NobleBlack.


# In[ ]:




