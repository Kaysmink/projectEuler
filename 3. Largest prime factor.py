# -*- coding: utf-8 -*-
"""
Created on Mon Jul 22 19:50:18 2019

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
goal=600851475143  

prime_factors=[]
while(is_prime(goal)==False):
    deviator=2
    while(is_prime_factor(goal, deviator)==False): 
        deviator=deviator+1
    prime_factors.append(deviator)
    goal=int(goal/deviator)
prime_factors.append(goal)

print(max(prime_factors))
print("Running time is: ",round(time.time()-start,4), "Seconds")
#Running time is 0.004 seconds







