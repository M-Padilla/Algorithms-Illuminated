# -*- coding: utf-8 -*-
"""
Created on Thu Feb  4 12:30:43 2021

@author: user
"""


def mergesort(array):
    '''
    Algorithm works by recursively splitting vectors in half, until reaching
    a base case of size 1. Then it goes all the way back by ordering pairs of
    vectors and merging them.
    '''
    
    
    def split(array):
        if len(array)!=1:
            #Split the array in 2 halves, if its size is greater than 1
            half= len(array)//2
            #Try to split both halves further, applying recursion
            L,R= split(array[:half]), split(array[half:])
            return merge(L,R) #Merge the ordered halves
        else:
            #If the array cannot be halved further, go back.
            return array


    def merge(array1,array2):
        #Takes 2 ordered arrays and merges them in order.
        B=[]
        i,j=0,0
        
        for k in range(len(array1)+len(array2)):
            if array1[i] <= array2[j]:
                B.append(array1[i])
                i+=1
            else:
                B.append(array2[j])
                j+=1
            if i>=len(array1) or j>=len(array2):
                #If the index of a vector is out of bounds (meaning that the
                #whole vector has been merged into B), this will merge the 
                #remaining elements from the other vector.
                if i>=len(array1):
                    B.extend(array2[j:])
                else:
                    B.extend(array1[i:])
                break
        return B
        
    
    return split(array) #PARENT LEVEL