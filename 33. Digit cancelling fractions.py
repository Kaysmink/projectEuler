# -*- coding: utf-8 -*-
"""
Created on Wed Jul 31 15:33:11 2019

@author: kaysm
"""
import time 
import math

start=time.time()

product=[1,1]
for i in range(10,100):
    denominator=i
    for j in range(10,i):
        numerator=j
        value=j/i
        den=str(i)
        num=str(j)
        same_number=set(list(den)).intersection(set(list(num))) #Find same number
        if(len(same_number)>0):
            same_number=same_number.pop()            
            den=int(den.replace(same_number,"",1))  #delete same number
            num=int(num.replace(same_number,"",1))  #delete same number          
            if(num>0 and den> 0 and num/den==j/i and int(same_number)>0): #check if fraction is still the same
                product[0]=product[0]*j
                product[1]=product[1]*i
         
result=int(product[1]/math.gcd(product[0],product[1]))
        
print(result)
print("Running time is: ",round(time.time()-start,4), "Seconds")
#running time is 0.01 seconds   