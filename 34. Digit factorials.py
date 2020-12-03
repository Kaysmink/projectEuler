# -*- coding: utf-8 -*-
"""
Created on Sat Jul 20 19:16:47 2019

@author: kaysm
"""

import math
import time

start=time.time()
Sum=0

for i in range(3,7*math.factorial(9)):
    digits=list(map(int,list(str(i))))
    Sum_of_digits=sum([math.factorial(value) for value in digits])
    if(Sum_of_digits==i):
        print(i)
        Sum=Sum+i

print(Sum)
print("Running time is: ",round(time.time()-start,2), "Seconds")
#Running time is 18.26 Seconds