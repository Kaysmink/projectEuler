# -*- coding: utf-8 -*-
"""
Created on Thu Jul 18 14:02:29 2019

@author: kaysm
"""
import time

start=time.time()

number=2**1000
print(sum(list(map(int,list(str(number))))))

print("Running time is: ",round(time.time()-start,4), "Seconds")
#Running time is 0.001 Seconds