# -*- coding: utf-8 -*-
"""
Created on Tue Mar 2 09:48:58 2021

@author: user
"""

def secondlargest(array):

    def split(array, keep_comparisons=True):
        # The keep_comparisons parameter enables tracking of the previous comparisons
        # of a number through an array
        if len(array)!=1:
            # Split the array of numbers in 2 halves, if its size is greater than 1
            half= len(array)//2 # Try to split both halves further, applying recursion
            L,R= split(array[:half], keep_comparisons), split(array[half:], keep_comparisons)
            return compare(L, R, keep_comparisons) #Compare the halves
        else:
            # If the array of numbers cannot be halved further, go back. 
            # If keep_comparison is true, returns a tuple with the number itself and a list of 
            # other numbers defeated by it in previous comparisons
            # Otherwise, it only returns the number.
            return (array[0], []) if keep_comparisons==True else array 
                
        
    def compare(array1, array2, keep_comparisons):
        greater_num, lesser_num = (array1, array2) if array1[0] >= array2[0] else (array2, array1)
        if keep_comparisons == True:
            # If keep_comparison is true, append the lesser number to the list of number defeated by the greater one.
            greater_num[1].append(lesser_num[0])
        return greater_num # Otherwise just returns the greater number.

                
    losers_array= split(array)[1] # Retrieve the list of elements defeated by the maximum element.
    
    # Select the maximum of the list of elements defeated by the maximum element: That's the second largest element.
    return split(losers_array, keep_comparisons=False)[0]
