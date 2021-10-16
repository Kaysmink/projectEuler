# -*- coding: utf-8 -*-
"""
Created on Thu Aug  8 21:35:18 2019

@author: kaysm
"""

import numpy
import time 

def is_prime(number):
    if(number==1):
        return False
    for j in range(2,int(number**0.5+1)):
        if(number%j==0):
            return False
    return True

def is_module_zero(goal, deviator):
    if(goal%deviator==0):
        return True
    return False

def is_prime_factor(goal, deviator):
    if(is_module_zero(goal, deviator)):
        if(is_prime(deviator)):
            return True
    return False


start=time.time()
results=[[1,1]]
for i in range(2,100001):
    goal=i
    set_of_prime_factors=set()
    while(is_prime(goal)==False):
        deviator=2
        while(is_prime_factor(goal, deviator)==False): 
            deviator=deviator+1
        set_of_prime_factors.add(deviator)
        goal=int(goal/deviator)    
    set_of_prime_factors.add(goal)
    rad=numpy.product(list(set_of_prime_factors))
    results.append([i,rad])

results=sorted(results, key=lambda x: x[1])
print(results[9999][0])   
    
print("Running time is: ",round(time.time()-start,4), "Seconds")
#Running time is 3,07 seconds