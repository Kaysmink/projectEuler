# -*- coding: utf-8 -*-
"""
Created on Fri Aug  2 16:12:02 2019

@author: kaysm
"""

from math import factorial as fac 
import time


Sn_list=[0]

def binomial_coefficients(n,k):
    return int(fac(n)/(fac(k)*fac(n-k)))

def B(n):
    product=1
    for k in range(0,n+1):
        product=product*binomial_coefficients(n,k)        
    return product

def is_devisor(number, i):
    if(number%i==0):
        return True
    return False

def D(n):
    Sum=0
    number=B(n)
    for i in range(1,number+1):
        if(is_devisor(number,i)):
            Sum=Sum+i
    return Sum   

start=time.time()
for i in range(1,8):
    Sn_list.append(Sn_list[-1]+D(i))   

print("Running time is: ",round(time.time()-start,4), "Seconds")
#Running time is 10.96 Seconds