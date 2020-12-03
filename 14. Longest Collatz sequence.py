# -*- coding: utf-8 -*-
"""
Created on Thu Jul 18 13:22:55 2019

@author: kaysm
"""
import time

start=time.time()
max_chain=0
result=0

d=1000000
lengths=["NA" for i in range(d)]
for i in range(1,d):
    if(i%2==0):
        length=lengths[int(i/2)]+1
        lengths[i]=length
        #print(i, length)        
    else:    
        length=1
        number=i 
        while(number!=1):
            if(number<d and lengths[number]!= "NA"):
                length=lengths[number]+length-1
                break
            length=length+1
            if(number%2==0):
                number=number/2
            else:
                number=(number*3)+1
            number=int(number)
        lengths[i]=length
        if(length>max_chain):
            max_chain=length
            result=i
        
print("Running time is: ",round(time.time()-start,4), "Seconds")
#Running time is 4.11 seconds   
        