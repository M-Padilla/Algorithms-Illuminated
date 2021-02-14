# -*- coding: utf-8 -*-
"""
Created on Wed Feb  3 21:52:09 2021

@author: user

Assumptions:
    *Both numbers are integers.
"""


import math #Cannot use NumPy as it requires float numbers in a lot of steps.


def karatsuba(num1,num2):
    '''
    Applies the Karatsuba algorithm for fast multiplication, discovered by
    Anatoly Karatsuba in 1960.
    '''
    
    #Get number of digits. Use conditional in case num1==0, as 0 is outside the
    #log10 function's domain.
    N= max(math.floor(math.log10(num1)+1),math.floor(math.log10(num2)+1)) if (num1 != 0 and num2!=0) else 1
    half_N= math.ceil(N/2)
    
    if N!=1:
        #Get the left halves of each number
        a = math.floor(num1 / (10**(half_N)))
        c = math.floor(num2 / (10**(half_N)))
        #Get the right halves of each number
        b = num1 % (10**(half_N))
        d = num2 % (10**(half_N))
        #Now calculate a*c, b*d and p*q by recursive call on each multiplication
        #term
        ac= karatsuba(a,c)
        bd= karatsuba(b,d)
        #Sum the halves of each number and multiply
        #p = a+b, q = c+d
        pq= karatsuba(a+b,c+d) 
        #Calculate ad+bc through (a+b)(c+d)-ac-bd = ad+bc
        adbc= pq-ac-bd #Notice that p=(a+b) and q=(c+d)
        '''
        Add trailing zeroes to the products by positional value, taking into
        #account that x*y = ((10**ceil(n/2))*a + b) · ((10**ceil(n/2))*c + d)
                          =  (10**(2*ceil(n/2)) * (a*c) + (10**ceil(n/2)) * (a*d + b*c) + (b*d)
        This saves 1 recursive call.
        '''
        return int((10**(half_N*2))*ac + (10**(half_N))*adbc + bd)
        #The above could be done by Karatsuba too, but let's be serious.    
        
    else:
        #If N=1, both numbers are digits and the multiplication is evaluated
        #directly
        return(num1*num2)