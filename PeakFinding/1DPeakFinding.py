#!/usr/bin/env python
# coding: utf-8

# PEAK-FINDING PROBLEM FOR 1-D ARRAY USING BINARY-SEARCH ALGORITHM IN Log(n) time
# 

# In[5]:


from random import randint 

##a=list(map(int,input().split()))

#Input of 1DArray using function randint()
def Array1D(n): 
    arr=[]
    for i in range(n):
        arr.append(randint(1,100))
    return arr

#Finding Local Peak
def FindPeak1D(arr):
    if arr[0]>=arr[1]:
        return 0,arr[0]
    elif arr[-1]>=arr[-2]:
        return len(arr)-1,arr[-1]
    return Peak1D(arr,0,len(arr)-1)

#Finding Peak using Recursion
def Peak1D(arr,start,end):
    mid=start+(end-start)//2
    if start==end:
        return mid,arr[mid]
    elif arr[mid]<arr[mid+1]:
        return Peak1D(arr,mid+1,end)
    elif arr[mid]<arr[mid-1]:
        return Peak1D(arr,0,mid-1)
    else:
        return mid,arr[mid]



# In[2]:


#Driver-Code
n=int(input("Input size of array"))
arr=Array1D(n)
print(arr)
index,peak = FindPeak1D(arr)
print(index,peak)
#print(element)
                    ###Contributed by NobleBlack. 


# In[ ]:





# In[ ]:





# In[ ]:




