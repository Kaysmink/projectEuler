# -*- coding: utf-8 -*-
"""
Created on Thu Jul 18 17:25:41 2019

@author: kaysm
"""

import math
import time

start=time.time()

value=math.factorial(100)
print(sum(list(map(int,list(str(value))))))

print("Running time is: ",round(time.time()-start,4), "Seconds")
#Running time is 0.001 Seconds