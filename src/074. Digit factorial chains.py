# -*- coding: utf-8 -*-
"""
Created on Sat Jul 27 21:33:55 2019

@author: kaysm
"""

import math 
import itertools as it
import time

def next_number(number):
    number=str(number)
    Sum=0
    for value in number:
        Sum=Sum+math.factorial(int(value))
    return Sum

start=time.time()
result=0
visits=["NA" for i in range(1000000)]
for i in range(0,1000000):
    if(visits[i]=="NA"):
        number=i
        chain=[number]
        
        while(next_number(number) not in chain):
            number=next_number(number)
            chain.append(number)

        perm_list=[]
        for perm in it.permutations(str(i)):
            if(int("".join(perm)) not in perm_list):
                perm_list.append(int("".join(perm)))                
                if(len(chain)==60 and visits[int("".join(perm))]=="NA"):
                    result=result+1
                visits[int("".join(perm))]=True    
         
print(result)      
print("Running time is: ",round(time.time()-start,4), "Seconds")
#Running time is 16.99 Seconds