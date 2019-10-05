#!/usr/bin/env python
# coding: utf-8

# PEAK-FINDING PROBLEM FOR 2-D ARRAY USING IN nLog(n) time

# In[1]:


from random import randint
#Input for 2DArray using function randint
def Array2D(n,m):
    arr=[[randint(1,1000) for i in range(m)] for j in range(n)]
    return arr

#Function to extract Global-Maxima for each Column intake
def Maxima(arr,mid):
    a=[row[mid] for row in arr]
    i=a.index(max(a))
    return i

#Function to fine 2DArray-Peak
def FindPeak2D(arr,n,m):
    return Peak2D(arr,0,m-1,n)

#Function for finding 2DPeak using Recursion
def Peak2D(arr,start,end,n):
    mid=start + (end-start)//2
    index=Maxima(arr,mid)
    if start == end:
        return index,mid,arr[index][mid]
    if arr[index][mid] < arr[index][mid+1]:
        return Peak2D(arr,mid+1,end,n)
    elif arr[index][mid] < arr[index][mid-1]:
        return Peak2D(arr,0,mid-1,n)
    else:
        return index,mid,arr[index][mid]
    


# In[9]:


#Driver-Code for Finding 2DPeak
n,m=map(int,input("Input No of Rows and Columns").split())
arr=Array2D(n,m)
#print(arr)
x,y,element=FindPeak2D(arr,n,m)
element
                ###Contributed by NobleBlack.


# In[12]:





# In[13]:





# In[ ]:




