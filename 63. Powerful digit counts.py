# -*- coding: utf-8 -*-
"""
Created on Fri Jul 26 13:21:03 2019

@author: kaysm
"""

import time 

def calculate_number_of_ith_powers(n):
    ith_powers=0
    j=1
    while(len(str(j**n))<=i):
        if(len(str(j**n))==i):
            ith_powers=ith_powers+1
        j=j+1    
    return ith_powers

start=time.time()

i=1
num_of_numbers=0
while(calculate_number_of_ith_powers(i)>0):
    num_of_numbers=num_of_numbers+calculate_number_of_ith_powers(i)
    i=i+1

print(num_of_numbers)
print("Running time is: ",round(time.time()-start,4), "Seconds")
#Running time is 0.001 Seconds
    