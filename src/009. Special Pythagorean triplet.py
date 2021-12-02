# -*- coding: utf-8 -*-
"""
Created on Wed Jul 17 21:10:59 2019

@author: kaysm
"""
import math
import time

start=time.time()

possibilities=[]
for a in range(1,1000):
    for b in range(1,1000):
        c=math.sqrt(a*a +b*b)
        if(c%1==0):
            possibilities.append([a,b,int(c)])

for pair in possibilities:
    if(sum(pair)==1000):
        product=1
        for number in pair:
            product=product*number
        print(product)
        break
    
print("Running time is: ",round(time.time()-start,4), "Seconds")
#Running time is 1.03 seconds