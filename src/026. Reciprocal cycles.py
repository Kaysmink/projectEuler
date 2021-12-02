# -*- coding: utf-8 -*-
"""
Created on Tue Jul 30 20:54:00 2019

@author: kaysm
"""

import time 

start=time.time()

d=1000
num_of_remainders=[0 for i in range(d)]
for i in range(2,d):
    remainders=[]
    remainder=1
    
    while(True):
        if(remainder in remainders):
            break        
        remainders.append(remainder)    
        remainder=(remainder*10)%i
    num_of_remainders[i]=len(remainders)        

print(num_of_remainders.index(max(num_of_remainders)))   
    
print("Running time is: ",round(time.time()-start,4), "Seconds")
#running time is 0.35 seconds   
    
    
