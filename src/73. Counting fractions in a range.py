# -*- coding: utf-8 -*-
"""
Created on Thu Oct 14 15:42:58 2021

@author: kaysm
"""

import math
import time

starttime = time.time()
numOfFractions = 0
maxD = 12000
for d in range(1, maxD+1):
    for n in range(d//3,d//2 +1):
        if n == 0:
            continue
        fraction = n/d
        if 1/3 < fraction < 1/2 and math.gcd(n, d) == 1:
            numOfFractions = numOfFractions + 1

print(numOfFractions)
            
print("Running time is: ",round(time.time()-starttime,4), "Seconds")
#Running time is 12.272 seconds