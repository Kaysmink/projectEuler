# -*- coding: utf-8 -*-
"""
Created on Tue Jul 30 18:42:30 2019

@author: kaysm
"""

import time 

def check_digits(number):
    number=list(str(number))
    number=set(list(map(int,number)))
    if(max(number)<=2):
        return True
    return False

def f(n):
    if(n%9==0):
        if(precomputed[9]%n==0):
            return precomputed[9]/n
    if(n%99==0):
        if(precomputed[99]%n==0):
            return precomputed[99]/n
    if(n%999==0):
        if(precomputed[999]%n==0):
            return precomputed[999]/n
    i=1
    while(True):
        number=n*i
        if(check_digits(number)):
            break
        i=i+1
    return number/n

start=time.time()
precomputed={9:12222, 99:1122222222, 999:111222222222222, 9999:11112222222222222222}

Sum=0
for i in range(1,100):
    print(i)
    Sum=Sum+f(i)
print(Sum)
print("Running time is: ",round(time.time()-start,4), "Seconds")
#Running time is infinity