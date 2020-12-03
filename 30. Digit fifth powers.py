# -*- coding: utf-8 -*-
"""
Created on Sat Jul 20 19:06:55 2019

@author: kaysm
"""
import time 

start=time.time()

Sum=0
for i in range(2,355000):
    digits=list(map(int,list(str(i))))
    Sum_of_digits=sum([value**5 for value in digits])
    if(Sum_of_digits==i):
        Sum=Sum+i
        
print("Running time is: ",round(time.time()-start,4), "Seconds")
#Running time is 3.30 Seconds

    