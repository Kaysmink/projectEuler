# -*- coding: utf-8 -*-
"""
Created on Thu Jul 18 17:29:55 2019

@author: kaysm
"""

import time

def find_Sum_of_devisors(number):
    Sum=0
    for i in range(1,int(number/2)+1):
        if(number%i==0):
            Sum=Sum+i
    return Sum

start=time.time()

Amicable=[]
for i in range(0,10000):
    Sum=find_Sum_of_devisors(i)
    if(find_Sum_of_devisors(Sum)==i and Sum!=i):
        if(i not in Amicable):
            Amicable.append(i)
            if(Sum not in Amicable):
                Amicable.append(Sum)
print(Amicable)
print(sum(Amicable))

print("Running time is: ",round(time.time()-start,4), "Seconds")
#Running time is 3.62 Seconds
        