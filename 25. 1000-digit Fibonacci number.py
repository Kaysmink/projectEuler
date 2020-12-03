# -*- coding: utf-8 -*-
"""
Created on Fri Jul 19 20:38:36 2019

@author: kaysm
"""

import time 

start=time.time()

imin1=1
imin2=1

index=2
while(True):
    new=imin1+imin2
    imin2=imin1
    imin1=new
    index=index+1
    
    if(len(str(new))==1000):
        print(index)
        break
        
print("Running time is: ",round(time.time()-start,4), "Seconds")
#Running time is 0.06 Seconds