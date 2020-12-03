# -*- coding: utf-8 -*-
"""
Created on Wed Jul 31 14:39:45 2019

@author: kaysm
"""

import time 

def is_prime(number):
    if(number<=0):
        return False
    if(number==1):
        return False
    for j in range(2,int(number**0.5+1)):
        if(number%j==0):
            return False
    return True

def formula(n,a,b):
    value=n**2 + a*n + b
    return value

start=time.time()

range_a=range(-999,1000)
range_b=range(-1000,1001)

most_consecutives=0

for a in range_a:
    for b in range_b:
        n=0
        consecutives=0
        number=int(formula(n,a,b))
        while(is_prime(number)):
            consecutives=consecutives+1
            n=n+1
            number=formula(n,a,b)
        if(consecutives>most_consecutives):
            most_consecutives=consecutives
            final_a=a
            final_b=b

print(final_a*final_b)
print("Running time is: ",round(time.time()-start,4), "Seconds")
#running time is 8.31 seconds   












