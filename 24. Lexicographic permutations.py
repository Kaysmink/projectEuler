# -*- coding: utf-8 -*-
"""
Created on Fri Jul 19 20:24:46 2019

@author: kaysm
"""
import itertools as it
import time

start=time.time()

i=0
for permutation in it.permutations(range(10)):
    i=i+1
    if(i==1000000):
        print("".join(list(map(str,permutation))))
        break
    
print("Running time is: ",round(time.time()-start,4), "Seconds")
#Running time is 0.43 Seconds