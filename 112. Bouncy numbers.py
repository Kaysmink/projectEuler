# -*- coding: utf-8 -*-
"""
Created on Fri Jul 26 11:37:29 2019

@author: kaysm
"""

import time

def is_bouncy(number):
    if(is_increasing(number)==True or is_decreasing(number)==True):
        return False
    return True
    
def is_increasing(number):
    number=str(number)
    for i in range(1,len(number)):
        if(number[i-1]>number[i]):
            return False
    return True

def is_decreasing(number):
    number=number=str(number)
    for i in range(0,len(number)-1):
        if(number[i]<number[i+1]):
            return False
    return True


start=time.time()
num_bouncy=0
num_not_bouncy=0

is_increasing(0)
i=0
while(True):
    if(is_bouncy(i)):
        num_bouncy=num_bouncy+1
    else:
        num_not_bouncy=num_not_bouncy+1
    proportion=num_bouncy/(num_not_bouncy+num_bouncy)*100
    if(proportion>=99):
        break
    i=i+1
    
print(i)
print("Running time is: ",round(time.time()-start,4), "Seconds")
#Running time is 4.87 seconds    

