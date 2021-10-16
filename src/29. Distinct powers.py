# -*- coding: utf-8 -*-
"""
Created on Sat Jul 20 18:57:28 2019

@author: kaysm
"""
import time 

start=time.time()

values=[]
for a in range(2,101):
    for b in range(2,101):
        values.append(a**b)

print(len(list(set(values))))

print("Running time is: ",round(time.time()-start,4), "Seconds")
#Running time is 0.01 Seconds