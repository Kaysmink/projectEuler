# -*- coding: utf-8 -*-
"""
Created on Wed Jul 17 20:03:53 2019

@author: kaysm
"""
import time
start=time.time()
for i in range(20,200000000000,20):
    if(i %  2 == 0 and i %  3 == 0 and i %  4 == 0 and i %  5 == 0 and
         i %  6 == 0 and i %  7 == 0 and i %  8 == 0 and i %  9 == 0 and
         i % 10 == 0 and i % 11 == 0 and i % 12 == 0 and i % 13 == 0 and
         i % 14 == 0 and i % 15 == 0 and i % 16 == 0 and i % 17 == 0 and
         i % 18 == 0 and i % 19 == 0 and i % 20 == 0):
        print(i)
        break
print("Running time is: ",round(time.time()-start,4), "Seconds")
#Running time is 7,98 seconds