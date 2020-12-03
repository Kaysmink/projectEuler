# -*- coding: utf-8 -*-
"""
Created on Wed Jul 31 17:04:20 2019

@author: kaysm
"""

def triangular(n):
    return int((n*(n+1)/2))

def hexagonal(n):
    return int(n*(2*n-1))

def pentagonal(n):
    return int((n*(3*n-1)/2))

def is_pentagonal(number, n):
    while(pentagonal(n)<number):
        n=n+1
    if(pentagonal(n)==number):
        return True
    return False

def is_triangular(number, n):
    while(triangular(n)<number):
        n=n+1
    if(triangular(n)==number):
        return True
    return False

import time

start=time.time()
i=144
while(True):
    number=hexagonal(i)
    if(is_pentagonal(number,i) and is_triangular(number,i)):
        print(number)
        break
    i=i+1    
    
print("Running time is: ",round(time.time()-start,4), "Seconds")
#running time is 39,19 seconds   

    