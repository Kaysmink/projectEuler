# -*- coding: utf-8 -*-
"""
Created on Thu Aug  1 17:22:06 2019

@author: kaysm
"""

import time 

def are_permuatation(one, two, three):
    if(set(list(one))==set(list(two))==set(list(three))):
        return True
    return False

def is_prime(number):
    if(number==1):
        return False
    for j in range(2,int(number**0.5+1)):
        if(number%j==0):
            return False
    return True

start=time.time()

for i in range(9999, 7659,-2):
    if(is_prime(i)==True):
        large=i
        second=i-3330
        smallest=i-2*3330
        
        if(is_prime(large)==is_prime(second)==is_prime(smallest)==True):   
            if(are_permuatation(str(large), str(second), str(smallest))):
                print(str(smallest)+str(second)+str(large))
                break

print("Running time is: ",round(time.time()-start,4), "Seconds")
#Running time is 0.001 seconds   
        