# -*- coding: utf-8 -*-
"""
Created on Sat Aug  3 21:20:31 2019

@author: kaysm
"""

import time 

def is_prime(number):
    if(number==1):
        return False
    for j in range(2,int(number**0.5+1)):
        if(number%j==0):
            return False
    return True

def all_devisors_are_prime(n):
    if(is_prime(n+1)==False):
        return False
    for d in range(1,int(n/2)+1):
        if(n%d==0):
            formula_number=d+n/d
            if(is_prime(formula_number)==False):
                return False
    return True

start=time.time()
Sum=0
for i in range(1,1000000):
    if(all_devisors_are_prime(i)):
        Sum=Sum+i
        
print(Sum)
print("Running time is: ",round(time.time()-start,4), "Seconds")
#Running time is 13.38 seconds