# -*- coding: utf-8 -*-
"""
Created on Thu Jul 18 12:35:36 2019

@author: kaysm
"""

import math
import time
numbers=[1]

start=time.time()
for x in range(0,1000000):
    number=int(x*(x+1)/2)
    if(math.sqrt(number)*math.sqrt(number)==number):
        NumOfFactors=-1
    else:
        NumOfFactors=0
    for i in range(1,int(math.sqrt(number)+1)):
        if(number%i==0):
            NumOfFactors=NumOfFactors+2
    if(NumOfFactors>500):
        print(number)
        break
    
print("Running time is: ",round(time.time()-start,4), "Seconds")
#Running time is 14.84 seconds