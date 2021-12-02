# -*- coding: utf-8 -*-
"""
Created on Wed Jul 31 15:22:02 2019

@author: kaysm
"""

import time 

start=time.time() 

target=200
result=0
for a in range(target,-1, -200):
    for b in range(a, -1, -100):
        for c in range(b, -1, -50):
            for d in range(c, -1, -20):
                for e in range(d, -1, -10):
                    for f in range(e, -1, -5):
                        for g in range(f, -1, -2):
                            result=result+1

print(result)
print("Running time is: ",round(time.time()-start,4), "Seconds")
#running time is 0.01 seconds   
