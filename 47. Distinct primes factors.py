# -*- coding: utf-8 -*-
"""
Created on Thu Aug  1 17:02:58 2019

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


def find_prime_factors(number):    
    prime_factors=[]
    while(is_prime(number)==False):
        deviator=2
        while(is_prime_factor(number, deviator)==False): 
            deviator=deviator+1
        prime_factors.append(deviator)
        number=int(number/deviator)
    prime_factors.append(number)
    return(prime_factors)

start=time.time()

i=2
while(True):
    one=set(find_prime_factors(i))
    two=set(find_prime_factors(i+1))
    three=set(find_prime_factors(i+2))
    four=set(find_prime_factors(i+3))
    
    if(len(three)==len(two)==len(one)==len(four)==4):
            if(one.intersection(two).intersection(three).intersection(four)==set()):
                print(i)
                break
    i=i+1
    
print("Running time is: ",round(time.time()-start,4), "Seconds")
#Running time is 13.38 seconds





