# -*- coding: utf-8 -*-
"""
Created on Tue Jul 23 12:47:40 2019

@author: kaysm
"""
import time 

start=time.time()

i=1
while(True):
    one=sorted(list(str(i)))
    two=sorted(list(str(i*2)))
    three=sorted(list(str(i*3)))
    four=sorted(list(str(i*4)))
    five=sorted(list(str(i*5)))
    six=sorted(list(str(i*6)))
    
    if(one==two==three==four==five==six):
        print(i)
        break
    i=i+1
    
print("Running time is: ",round(time.time()-start,4), "Seconds")
#Running time is 1.70 Seconds