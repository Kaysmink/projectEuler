# -*- coding: utf-8 -*-
"""
Created on Fri Jul 26 13:48:24 2019

@author: kaysm
"""

import time 

def calculate_new_number(number):
    Sum=0
    for i in range(0,len(str(number))):
        Sum=Sum+int(str(number)[i])**2    
    return Sum


start=time.time()
n=10000000
arrive=["NA" for i in range(n+1)]
arrive[0]=False
arrive[1]=False
arrive[89]=True

for i in range(1,n+1):
    if(arrive[i]=="NA"):
        print(i)
        number=i
        chain=[number]
        while(True):
            number=calculate_new_number(number)
            chain.append(number)
            if(arrive[number]==False):
                for value in chain:
                    arrive[value]=False
                break
            if(arrive[number]==True):
                for value in chain:
                    arrive[value]=True
                break
    else: 
        continue
    
print(arrive.count(True))
print("Running time is: ",round(time.time()-start,4), "Seconds")
#Running time is 1106.07 Seconds !!!



