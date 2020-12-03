# -*- coding: utf-8 -*-
"""
Created on Tue Jul 23 21:36:30 2019

@author: kaysm
"""

import math 
import time

def find_relative_primes(number):
    num_of_relative_primes=len([i for i in range(1,number) if(math.gcd(i,number)==1)])  
    return num_of_relative_primes
          
start=time.time()
max_value=0
number=0
for i in range(2,1000000):
    num_of_relative_primes=find_relative_primes(i)
    if((i/num_of_relative_primes)>max_value):
        max_value=i/find_relative_primes(i)
        number=i
    
    
print(number)
print("Running time is: ",round(time.time()-start,4), "Seconds")
#Running time is infinity
            
"""Code is taking way to long time, but does work"""