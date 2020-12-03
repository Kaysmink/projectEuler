# -*- coding: utf-8 -*-
"""
Created on Mon Jul 22 20:58:22 2019

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

start=time.time()
goal=10001
num_of_primes=0
for i in range(2,10000000):
    if(is_prime(i)):
        num_of_primes=num_of_primes+1
    if(num_of_primes==goal):
        print(i)
        break
print("Running time is: ",round(time.time()-start,4), "Seconds")
#Running time is 0.58 seconds  
    