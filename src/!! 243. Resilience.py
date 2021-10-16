# -*- coding: utf-8 -*-
"""
Created on Fri Aug  2 13:52:21 2019

@author: kaysm
"""

import time
import math

def is_prime(number):
    if(number==1):
        return False
    for j in range(2,int(number**0.5+1)):
        if(number%j==0):
            return False
    return True

def can_be_cancelled_down(numerator, denominator):
    if(math.gcd(numerator,denominator)==1):
        return False
    return True


def Rd(denominator):
    resilience=0
    if(is_prime(denominator-1)==False):
        return 1        
    for numerator in range(1,denominator):
        if(can_be_cancelled_down(numerator, denominator)==False):
            resilience=resilience+1
    return resilience/(denominator-1)

start=time.time()

goal=4/10
primes=[2,3,5,7,11,13,17,19,23]
denominator=2
find=True
while(find):
    for prime in primes:
        number=denominator*prime
        rd=Rd(number)
        if(rd<goal):
            print(number)
            find=False
            break
    denominator=denominator+1

print("Running time is: ",round(time.time()-start,4), "Seconds")
#Running time is infinity seconds   