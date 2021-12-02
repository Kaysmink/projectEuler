# -*- coding: utf-8 -*-
"""
Created on Sat Aug  3 20:40:36 2019

@author: kaysm
"""

import math
import time 

start=time.time()  

num_of_solutions=[0 for i in range(0,1001)]

for i in range(1000):
    for j in range(1000):
        if(i+j>1000):
            break
        x=math.sqrt(i**2+j**2)
        perimeter=i+j+x
        if(perimeter%1==0 and i!=0 and j!=0 and perimeter<1001):
            perimeter=int(perimeter)
            num_of_solutions[perimeter]=num_of_solutions[perimeter]+0.5

max_value=max(num_of_solutions)
print(num_of_solutions.index(max_value))
print("Running time is: ",round(time.time()-start,4), "Seconds")
#Running time is 0.84 Seconds
