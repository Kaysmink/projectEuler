# -*- coding: utf-8 -*-
"""
Created on Fri Jul 26 13:07:32 2019

@author: kaysm
"""

import math
import time 

start=time.time()

values=0
for i in range(1,101):
    for j in range(1,i+1):
        num_of_permutations=math.factorial(i)/(math.factorial(j)*math.factorial(i-j))
        if(num_of_permutations>1000000):
            values=values+1
            
print(values)

print("Running time is: ",round(time.time()-start,4), "Seconds")
#Running time is 0.02 Seconds
        