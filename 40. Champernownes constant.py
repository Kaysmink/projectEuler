# -*- coding: utf-8 -*-
"""
Created on Tue Jul 23 12:20:07 2019

@author: kaysm
"""
import time 

start=time.time()

num=""
for i in range(1,1000001):
    number=str(i)
    num=num+number
    
product=int(num[0])*int(num[9])*int(num[99])*int(num[999])*int(num[9999])*int(num[99999])*int(num[999999])

print(product)
print("Running time is: ",round(time.time()-start,4), "Seconds")
#Running time is 4.85 Seconds