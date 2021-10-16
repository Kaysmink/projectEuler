# -*- coding: utf-8 -*-
"""
Created on Fri Aug  2 20:43:30 2019

@author: kaysm
"""

import time 

def find_streak(n):
    streak=0
    k=1
    while(n%k==0):        
        streak=streak+1
        k=k+1
        n=n+1
    return streak

def P(s,N):
    result=0
    for n in range(2,N):
        if(find_streak(n)==s):
            result=result+1
    return result

start=time.time()

Sum=0
for i in range(1,11):
    print(i)
    Sum=Sum+P(i,4**i)

print(Sum)
print("Running time is: ",round(time.time()-start,4), "Seconds")
#Running time is 10.96 Seconds
