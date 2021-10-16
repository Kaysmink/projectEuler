# -*- coding: utf-8 -*-
"""
Created on Sat Jul 27 20:30:02 2019

@author: kaysm
"""

import time 

def is_form(number, desired):
    form=list(map(int,[str(number)[i] for i in range(0,len(str(number)),2)]))
    if(form==desired):
        return True
    return False

start=time.time()   
desired=[1,2,3,4,5,6,7,8,9,0]
highest_possible=int(1929394959697989990**0.5)

number=highest_possible
while(True):
    if(is_form(number**2, desired)==True):        
        break
    number=number-1

print(number)
print("Running time is: ",round(time.time()-start,4), "Seconds")
#Running time is 0.06 Seconds