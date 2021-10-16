# -*- coding: utf-8 -*-
"""
Created on Sat Jul 20 20:28:36 2019

@author: kaysm
"""
import time 

start=time.time()

Sum=0
def is_palindrome(n):
    reverse=n[::-1]
    if(n==reverse):
        return True
    return False
    
for i in range(1,1000000):
    binary=bin(i)[2:]
    if(is_palindrome(str(i)) and is_palindrome(binary)):
        Sum=Sum+i
        
print(Sum)

print("Running time is: ",round(time.time()-start,4), "Seconds")
#Running time is 1.80 Seconds
    

