# -*- coding: utf-8 -*-
"""
Created on Sat Feb  8 15:25:14 2020

@author: kaysm
"""

import time 
import math as m 

start=time.time()

def isPentagonal(N):       
    n = (1 + m.sqrt(24 * N + 1)) / 6
    if((n - int (n)) == 0):
        return [True , int(n)]
    return False

def nextPantgonal(n):
    return int(n*(3*n-1)/2)
    
pentagonalNumbers = []
n = 10000

for i in range(1,n):
    pentagonalNumbers.append(nextPantgonal(i))

diffrences = []
found = False
for i in range(0, n-1):
    for j in range(i, n-1):
        Sum = pentagonalNumbers[i] + pentagonalNumbers[j]
        if(isPentagonal(Sum)):
            dif = pentagonalNumbers[j] - pentagonalNumbers[i]
            if(isPentagonal(dif)):
                found = True
                print(dif)
                break
    if(found == True):
        break

print("Running time is: ",round(time.time()-start,4), "Seconds")
#Running time is 12,67 Seconds


