# -*- coding: utf-8 -*-
"""
Created on Tue Jul 23 20:54:58 2019

@author: kaysm
"""

import time

start=time.time()

max_sum=0
for a in range(0,100):
    for b in range(0,100):
        number=a**b
        Sum=sum(list(map(int,list(str(number)))))
        if(Sum>max_sum):
            max_sum=Sum
print(max_sum) 

print("Running time is: ",round(time.time()-start,4), "Seconds")
#Running time is 0.31 Seconds          

        
        
        