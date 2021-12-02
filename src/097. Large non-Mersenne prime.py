# -*- coding: utf-8 -*-
"""
Created on Wed Sep 29 16:23:48 2021

@author: kaysm
"""

import time 
start = time.time()

print((28433 * (pow(2,7830457)) + 1) % (10**10))

print("Running time is: ",round(time.time()-start,4), "Seconds")
#Running time is 0.0625 seconds

