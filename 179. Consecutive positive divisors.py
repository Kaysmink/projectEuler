# -*- coding: utf-8 -*-
"""
Created on Wed Aug  7 19:57:12 2019

@author: kaysm
"""
import time 
from functools import reduce

def num_of_factors(n):
        step = 2 if n%2 else 1
        return len(set(reduce(list.__add__,
                    ([i, n//i] for i in range(1, int(n**0.5)+1, step) if n % i == 0))))
        

start=time.time()

last=0
result=0
for i in range(2, 10**7+1):
    new=num_of_factors(i)
    if(last==new):
        result=result+1
    last=new
    
    if(i%100000==0):
        print(i)
        
    
print("Running time is: ",round(time.time()-start,4), "Seconds")
#Running time is 1600 Seconds!!!




    
    
    