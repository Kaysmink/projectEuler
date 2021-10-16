# -*- coding: utf-8 -*-
"""
Created on Thu Oct 14 16:03:38 2021

@author: kaysm
"""

from math import gcd
import time
from src.hulpfuncties.Find_primes_up_to_x import *

starttime = time.time()

maxD = 10000
primes = find_primes_up_to_x(maxD)
primes.append(1)

result = 0 
for d in range(1, maxD+1):
    devisors = [i for i in range(2,d) if d%i == 0]
    if d in primes:
        denoms = d-1
    else:
        denoms = [n for n in range(1, d) if gcd(n,d) == 1]
        #print(d, denoms)
        denoms = len(denoms)
    
    result = result + denoms
    
print(result)
            
print("Running time is: ",round(time.time()-starttime,4), "Seconds")
#Running time is 12.272 seconds





