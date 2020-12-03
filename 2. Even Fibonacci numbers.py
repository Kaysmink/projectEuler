# -*- coding: utf-8 -*-
"""
Created on Wed Jul 17 19:30:19 2019

@author: kaysm
"""
import time 
start=time.time()
sequence=[1,2]
even=[2]

value=2
i=2

while(True):
    value=sequence[-1]+sequence[-2]
    if(value>4000000):
        break
    sequence.append(value)
    
    if(value%2==0):
        even.append(value)

print(sum(even))  
print("Running time is: ",round(time.time()-start,6), "Seconds")
#Running time is 0.0001 seconds
    