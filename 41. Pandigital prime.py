# -*- coding: utf-8 -*-
"""
Created on Mon Jul 22 13:25:15 2019

@author: kaysm
"""

import time
import itertools as it 

def is_prime(number):
    if(number==1):
        return False
    for j in range(2,int(number**0.5+1)):
        if(number%j==0):
            return False
    return True

def is_pandigital(number):
    number=list(str(number))
    n=len(number)
    if("0" in number):
        return False
    max_number=max(list(map(int,number)))
    length=len((set(number)))
    if(length==max_number==n):
        return True
    return False

def find_max_pandigital_prime():
    for i in range(1,10):
        for perm in it.permutations("987654321"[i-1:]):
            number=int("".join(perm))
            if(is_prime(number)):
                print(number)
                return number
          
start=time.time()
find_max_pandigital_prime()
print("Running time is: ",round(time.time()-start,2), "Seconds")
#running time is 1.37 seconds

