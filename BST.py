#!/usr/bin/env python
# coding: utf-8

# #Implementation of BST(Binary Search Tree)

# In[114]:


#!/usr/bin/python36

import os
import subprocess as sp
from random import randint
from bisect import bisect, bisect_left, bisect_right
from heapq import heappush, heappop, heapify
from collections import Counter
import math


# In[115]:


class Node:
    def __init__(self,data):
        self.data=data
        self.leftChild=None
        self.rightChild=None
    


# In[122]:


class BST:
    COUNT=[10]
    def __init__(self):
        self.root=None
    
    def insert(self,data):
        #node=Node(data)
        if self.root is None:
            self.root=Node(data)
        else:
            self.insertNode(self.root,data)
    
    def insertNode(self,node,data):
        if data<node.data:
            if node.leftChild is None:
                node.leftChild=Node(data)
            else:
                self.insertNode(node.leftChild,data)
        else:
            if node.rightChild is None:
                node.rightChild=Node(data)
            else:
                self.insertNode(node.rightChild,data)
    
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
        space += BST.COUNT[0] 
        self.print2DUtil(root.rightChild, space)  
        print()  
        for i in range(BST.COUNT[0] , space): 
            print(end = " ")  
        print(root.data)  
        self.print2DUtil(root.leftChild, space)  
    
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
    
    def remove(self,data):
        if self.root is None:
            print("Tree is Empty")
        else:
            self.root = self.removeNode(self.root,data)
    
    def removeNode(self,node,data):
        if node is None:
            return None
        elif data < node.data:
            node.leftChild = self.removeNode(node.leftChild,data)
        elif data > node.data:
            node.rightChild = self.removeNode(node.rightChild,data)
        #it means,this is the node, to be deleted :)
        else: 
            if not node.leftChild and not node.rightChild:#node with no children
                print("Removing the node with no subtree...")
                del node
                return None
            if not node.leftChild:#node with only rightChild
                print("Removing the node with only right Subtree...")
                tempNode = node.rightChild
                del node
                return tempNode
            if not node.rightChild:#node with only leftChild
                print("Removing the node with only left Subtree...")
                tempNode = node.leftChild
                del node
                return tempNode
                #node with two children, to be removed :) -->
                ##there are two ways to delete node having two children,
                ##1.)By predecessor method=> find the largest node in left 
                    ##subtree and then swap that node with node to be deleted,
                    ##and we will land at either of first two cases.
                ##2.)By Successor method=> find the smallest node in right 
                    ##subtree and then swap that node with node to be deleted,
                    ##and we will land at either of first two cases. :)
            print("Removing the node with Two Subtree...")
            #predecessor = self.getPredecessor(node.leftChild)
            #node.data = predecessor.data
            #node.leftChild = self.removeNode(node.leftChild,predecessor.data)
            ###by Successor method-->
            successor = self.getSuccessor(node.rightChild)
            node.data = successor.data
            node.rightChild = self.removeNode(node.rightChild,successor.data)
        
        return node
            
            
            
    def getSuccessor(self,node):
        if node.leftChild:
            return self.getSuccessor(node.leftChild)
        return node
    
    def getPredecessor(self,node):
        if node.rightChild:
            return self.getPredecessor(node.rightChild)
        return node
                
                
                
            
            
        
            
    
        
      











# In[123]:


tree=BST()
tree.insert(12)
tree.insert(13)
tree.insert(5)
tree.insert(3)
tree.insert(33)
tree.insert(4)
tree.insert(6)
tree.insert(23)

print(tree.getMin())
print(tree.getMax())




tree.print2D()




tree.traversal()




tree.remove(12)




tree.print2D()


					###Contributed by nobleBlack



