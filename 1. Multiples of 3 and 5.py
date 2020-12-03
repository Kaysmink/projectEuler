# -*- coding: utf-8 -*-
"""
Created on Wed Jul 17 19:24:08 2019

@author: kaysm
"""
import time 
start=time.time()
numbers=[]

for i in range(1,1000):
    if(i%3 ==0 or i%5 ==0):
        numbers.append(i)
        
print(sum(numbers))
print("Running time is: ",round(time.time()-start,4), "Seconds")
#Running time is 0.001 seconds

