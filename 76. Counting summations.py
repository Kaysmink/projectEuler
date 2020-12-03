# -*- coding: utf-8 -*-
"""
Created on Thu Jul 25 11:40:35 2019

@author: kaysm
"""

import time 

start=time.time()

n=100
num_of_ways=[0 for i in range(0,n+1)]
num_of_ways[0]=1

for i in range(1,n):
    for j in range(i,n+1):
        num_of_ways[j]=num_of_ways[j]+num_of_ways[j-i]

print(n, "can be written as the sum of two positive integers in", num_of_ways[n], "ways")

print("Running time is: ",round(time.time()-start,4), "Seconds")
#Running time is 0.004 Seconds