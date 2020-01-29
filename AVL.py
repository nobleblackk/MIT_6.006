#!/usr/bin/env python
# coding: utf-8

# #Implementation of AVL Tree

# In[13]:


#!/usr/bin/python36

import os
import subprocess as sp
import math
from random import randint, randrange
from bisect import bisect, bisect_left, bisect_right
from collections import Counter
from heapq import heapify, heappop, heappush


# In[12]:


class Node:
    def __init__(self,data):
        self.data = data
        self.parent = None
        self.leftChild = None
        self.rightChild = None
        self.height = 0
        


# In[65]:


class AVL:
    COUNT = [10]
    def __init__(self):
        self.root = None
    
    def insertion(self,data):
        self.root = self.insertionNode(self.root,data)
    def insertionNode(self,node,data):
        if not node:
            return Node(data)
        elif data < node.data:
            node.leftChild = self.insertionNode(node.leftChild,data)
            node.leftChild.parent = node
        else:
            node.rightChild = self.insertionNode(node.rightChild,data)
            node.rightChild.parent = node
        node.height = max(self.getHeight(node.leftChild), self.getHeight(node.rightChild)) + 1
        return self.settleViolation(node,data) #To check whether there is any violation or not
    
    def settleViolation(self,node,data):
        balance = ( self.getHeight(node.leftChild) - self.getHeight(node.rightChild) )
        
        ###Case 1
        ###Left Left Heavy Situation --> Resolving by Right Rotation
        if balance > 1 and data < node.leftChild.data:
            print("Left Left Heavy Situation --> Resolving by Right Rotation")
            return self.rotationRight(node)
        
        ###Case 2
        ###Right Right Heavy Situation --> Resolving by Left Rotation
        if balance < -1 and data > node.rightChild.data:
            print("Right Right Heavy Situation --> Resolving by Left Rotation")
            return self.rotationLeft(node)
        
        ###Case 3
        ###Left Right Heavy Situation --> Resolving by First Left Rotation then Right Rotation
        if balance > 1 and data > node.leftChild.data:
            print("Left Right Heavy Situation --> Resolving by First Left Rotation then Right Rotation")
            node.leftChild = self.rotationLeft(node.leftChild)
            return self.rotationRight(node)
        
        ###Case 4
        ###Right Left Heavy Situation --> Resolving by First Right Rotation then Left Rotation
        if balance < -1 and data < node.rightChild.data:
            print("Right Left Heavy Situation --> Resolving by First Right Rotation then Left Rotation")
            node.rightChild = self.rotationRight(node.rightChild)
            return self.rotationLeft(node)
        
        return node ###When there is no voilation :) 
    
    
    
    def getHeight(self,node):
        if node == None:
            return -1
        else:
            return node.height
        
    def getBalance(self,node):
        if node == None:
            return 0
        else:
            return (self.getHeight(node.leftChild) - self.getHeight(node.rightChild))
    
    ###Right Rotation
    def rotationRight(self,node):
        tempLeftChild = node.leftChild
        t = node.leftChild.rightChild
        
        node.leftChild = t
        if t != None:
            t.parent = node
        tempLeftChild.rightChild = node
        if node != None:
            node.parent = tempLeftChild
        
        node.height = max(self.getHeight(node.leftChild), self.getHeight(node.rightChild)) + 1
        tempLeftChild.height = max(self.getHeight(node.leftChild), self.getHeight(node.rightChild)) + 1
        
        return tempLeftChild
    
    ###Left Rotation
    def rotationLeft(self,node):
        tempRightChild = node.rightChild
        t = node.rightChild.leftChild
        
        node.rightChild = t
        if t != None:    
            t.parent = node
        tempRightChild.leftChild = node
        if node != None:    
            node.parent = tempRightChild
        node.height = max(self.getHeight(node.leftChild), self.getHeight(node.rightChild)) + 1
        tempRightChild.height = max(self.getHeight(node.leftChild), self.getHeight(node.rightChild)) + 1
        
        return tempRightChild
            
    def getPredecessor(self,node):
        if node.rightChild != None:
            return self.getPredecessor(node.rightChild)
        return node.data
    
    def getSuccessor(self,node):
        if node.leftChild != None:
            return self.getSuccessor(node.leftChild)
        return node.data
    
    def traversal(self):
        print('''
                Please Write Order for Traversal:
                1.InOrder-Traversal
                2.PreOrder-Traversal
                3.PostOrder-Traversal
                ''')
        n=int(input())
        if n==1:
            self.inOrder()
        elif n==2:
            self.preOrder()
        elif n==3:
            self.postOrder()
            
    def inOrder(self):
        if self.root is None:
            print("Tree is Empty")
        else:
            print("InOrder-Traversal:")
            self.inOrderTraversal(self.root)
    
    def inOrderTraversal(self,node):
        if node.leftChild is not None:
            self.inOrderTraversal(node.leftChild)
        print(node.data)
        if node.rightChild is not None:
            self.inOrderTraversal(node.rightChild)
    
    def preOrder(self):
        if self.root is None:
            print("Tree is Empty")
        else:
            print("PreOrder-Traversal:")
            self.preOrderTraversal(self.root)
    
    def preOrderTraversal(self,node):
        print(node.data)
        if node.leftChild is not None:
            self.preOrderTraversal(node.leftChild)
        if node.rightChild is not None:
            self.preOrderTraversal(node.rightChild)
        
    def postOrder(self):
        if self.root is None:
            print("Tree is Empty")
        else:
            print("PostOrder-Traversal:")
            self.postOrderTraversal(self.root)
    
    def postOrderTraversal(self,node):
        if node.leftChild is not None:
            self.postOrderTraversal(node.leftChild)
        if node.rightChild is not None:
            self.postOrderTraversal(node.rightChild)
        print(node.data)
    
    def removal(self,data):
        if self.root == None:
            print("Tree is Empty :)")
            return
        else:
            self.root = self.removalNode(self.root,data)
            
    def getMin(self):
        if self.root is None:
            print("Tree is Empty")
        else:
            return self.getMinValue(self.root)
    
    def getMinValue(self,node):
        if node.leftChild is None:
            return node.data
        else:
            return self.getMinValue(node.leftChild)
    
    def getMax(self):
        if self.root is None:
            print("Tree is Empty")
        else:
            return self.getMaxValue(self.root)
    
    def getMaxValue(self,node):
        if node.rightChild is None:
            return node.data
        else:
            return self.getMaxValue(node.rightChild)
    ###Printing the Tree in 2D form
    def print2D(self) : 
        self.print2DUtil(self.root, 0) 
    

    def print2DUtil(self,root, space) : 
        if (root == None) : 
            return
        space += AVL.COUNT[0] 
        self.print2DUtil(root.rightChild, space)  
        print()  
        for i in range(AVL.COUNT[0] , space): 
            print(end = " ")  
        print(root.data)  
        self.print2DUtil(root.leftChild, space)
            
    def removalNode(self,node,data):
        if data < node.data:
            node.leftChild = self.removalNode(node.leftChild,data)
        elif data > node.data:
            node.rightChild = self.removalNode(node.rightChild,data)
        
        ###It is the node to be deleted
        else:
            ###Removing Leaf Node
            if node.leftChild == None and node.rightChild == None:
                print("Remvoing Leaf Node...")
                del node
                return None
            
            ###Removing Node having only LeftChild
            if node.rightChild == None:
                print("Removing Node having only LeftChild")
                tempNode = node.leftChild
                del node
                return tempNode
            
            ###Removing Node having only RightChild
            if node.leftChild == None:
                print("Removing Node having only RightChild")
                tempNode = node.rightChild
                del node
                return tempNode
            
            ###Removing Node having both LeftChild and RightChild
            print("Removing Node having both LeftChild and RightChild")
            """
            There are two ways to delete any Node having both LeftChild and
            RightChild =>
            1.By Successor Method -> Find out the Smallest Node in the Right
            SubTree, and Then Swap it with the Main Node, We will end up in the 
            first Two cases, which could be solved easily. :)
            
            2.By Predecessor Method -> Find out the Largest Node in the Left
            SubTree, and Then Swap it with the Main Node, We will end up in the
            first Two Cases, which could be solved easily. :)
            """
            
            #predecessor = self.getPredecessor(node.leftChild)
            #node.data = predecessor.data
            #node.leftChild = self.removalNode(node.leftChild,predecessor.data)
            
            successor = self.getSuccessor(node.rightChild)
            node.data = successor.data
            node.rightChild = self.removalNode(node.rightChild,successor.data)
        
        node.height = max(self.getHeight(leftChild), self.getHeight(rightChild)) + 1
        balance = self.getBalance(node)
        
        ###Here we can not use settleViolation() as we dont have the parameter data
        ###So, here we are using the modified settleViolation() <3
                                                               
        ###Case 1
        ###Left Left Heavy Situation --> Resolving by Right Rotation
        if balance > 1 and self.getBalance(node.leftChild) >= 0:
            print("Left Left Heavy Situation --> Resolving by Right Rotation")
            return self.rotationRight(node)
        
        ###Case 2
        ###Right Right Heavy Situation --> Resolving by Left Rotation
        if balance < -1 and self.getBalance(node.rightChild) <= 0:
            print("Right Right Heavy Situation --> Resolving by Left Rotation")
            return self.rotationLeft(node)
        
        ###Case 3
        ###Left Right Heavy Situation --> Resolving by First Left Rotation then Right Rotation
        if balance > 1 and self.getBalance(node.leftChild) < 0:
            print("Left Right Heavy Situation --> Resolving by First Left Rotation then Right Rotation")
            node.leftChild = self.rotationLeft(node.leftChild)
            return self.rotationRight(node)
        
        ###Case 4
        ###Right Left Heavy Situation --> Resolving by First Right Rotation then Left Rotation
        if balance < -1 and self.getBalance(node.rightChild) > 0:
            print("Right Left Heavy Situation --> Resolving by First Right Rotation then Left Rotation")
            node.rightChild = self.rotationRight(node.rightChild)
            return self.rotationLeft(node)
        
        return node ###When there is no voilation :) 
    
    
                        ###Contributed by NobleBlack
        
        


# In[66]:


avl = AVL()


# In[67]:


avl.insertion(2)


# In[68]:


avl.insertion(3)


# In[63]:


avl.traversal()


# In[64]:


avl.insertion(4)


# In[69]:


avl.print2D()


# In[ ]:




