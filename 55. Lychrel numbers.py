# -*- coding: utf-8 -*-
"""
Created on Tue Jul 23 20:39:28 2019

@author: kaysm
"""
import time 

def is_palindrome(n):
    reverse=n[::-1]
    if(n==reverse):
        return True
    return False

def reverse(number):
    return int(str(number)[::-1])

def is_lychrel(number):    
    for i in range(1,50):
        value=number+reverse(number)
        if(is_palindrome(str(value))):
            return False
        number=value
    return True

start=time.time()
num_of_lychrel=0
for i in range(0,10000):
    if(is_lychrel(i)):
        num_of_lychrel=num_of_lychrel+1

print(num_of_lychrel)  

print("Running time is: ",round(time.time()-start,4), "Seconds")
#Running time is 0.12 Seconds

       
        
        