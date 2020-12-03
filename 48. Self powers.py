# -*- coding: utf-8 -*-
"""
Created on Tue Jul 23 12:35:45 2019

@author: kaysm
"""

import time 

start=time.time()

Sum=0

for i in range(1,1000):
    Sum=Sum+i**i
    
Sum=str(Sum)

print(Sum[-10:])

print("Running time is: ",round(time.time()-start,4), "Seconds")
#Running time is 0.003 Seconds