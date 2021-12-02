# -*- coding: utf-8 -*-
"""
Created on Mon Jul 22 22:11:13 2019

@author: kaysm
"""

import itertools as it
import time 

def is_divisibility(number):
    for i in range(0, len(prime_numbers)):
        number="".join(list(number))
        sub_string=int(number[i+1:i+4])
        if(sub_string%prime_numbers[i]!=0):
            return False
    return True
  
start=time.time()

prime_numbers=[2,3,5,7,11,13,17]
Sum=0
for perm in it.permutations("0123456789"):
    if(is_divisibility(perm)):
        Sum=Sum+int(("".join(list(perm))))

print(Sum)       
print("Running time is: ",round(time.time()-start,4), "Seconds")
#Running time is 16.82 Seconds
        
            
    
    