# -*- coding: utf-8 -*-
"""
Created on Wed Jul 17 20:53:46 2019

@author: kaysm
"""
import time 

start=time.time()
squares=[]
numbers=[]
for i in range(0,101):
    squares.append(i*i)
    numbers.append(i)
    
diff=(sum(numbers)*sum(numbers))-sum(squares)
print(diff)
print("Running time is: ",round(time.time()-start,4), "Seconds")
#Running time is 0.001 seconds