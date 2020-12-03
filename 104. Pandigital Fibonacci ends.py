# -*- coding: utf-8 -*-
"""
Created on Mon Jul 29 13:24:53 2019

@author: kaysm
"""

import time
import math

def one_to_nine_pandigital(number):
    number=list(map(int,list(str(number))))
    if(all(items in number for items in [1,2,3,4,5,6,7,8,9])):
        return True
    return False    

start=time.time()

i=3
phi = 1.61803398875
old=1
new=1
while(True):
    fn=old+new
    old=new
    new=fn
    
    last=fn%1000000000
    
    if(one_to_nine_pandigital(last)):
        phi = (1 + math.sqrt(5)) / 2
        t = i * math.log10(phi) + math.log10(1/math.sqrt(5))
        first = int((pow(10, t - int(t) + 8)))
        if(one_to_nine_pandigital(first)):
            print(i)
            break
    i=i+1
   
print("Running time is: ",round(time.time()-start,4), "Seconds")
#running time is 28,73 seconds
    