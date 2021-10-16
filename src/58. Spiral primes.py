# -*- coding: utf-8 -*-
"""
Created on Fri Aug  2 15:11:28 2019

@author: kaysm
"""

import time

def is_prime(number):
    if(number==1):
        return False
    for j in range(2,int(number**0.5+1)):
        if(number%j==0):
            return False
    return True

start=time.time()

bottum_r_start=1
bottum_l_start=1
top_l_start=1
top_r_start=1
bottum_r_diff=8
bottum_l_diff=6
top_l_diff=4
top_r_diff=2

i=1
num_of_primes=0
total=1
while(True):
    i=i+1
    new=bottum_r_start+bottum_r_diff
    bottum_r_start=new
    bottum_r_diff=bottum_r_diff+8
    if(is_prime(new)):
        num_of_primes=num_of_primes+1
    
    new=bottum_l_start+bottum_l_diff
    bottum_l_start=new
    bottum_l_diff=bottum_l_diff+8
    if(is_prime(new)):
        num_of_primes=num_of_primes+1
    
    new=top_l_start+top_l_diff
    top_l_start=new
    top_l_diff=top_l_diff+8
    if(is_prime(new)):
        num_of_primes=num_of_primes+1
    
    new=top_r_start+top_r_diff
    top_r_start=new
    top_r_diff=top_r_diff+8
    if(is_prime(new)):
        num_of_primes=num_of_primes+1
        
    total=total+4
    
    if(num_of_primes/total<0.10):
        print(i*2-1)
        break
    
print("Running time is: ",round(time.time()-start,4), "Seconds")
#Running time is 10.96 Seconds



