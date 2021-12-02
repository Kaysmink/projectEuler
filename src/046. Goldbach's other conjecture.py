# -*- coding: utf-8 -*-
"""
Created on Fri Sep 17 12:11:44 2021

@author: kaysm
"""

from src.hulpfuncties.Find_primes_up_to_x import *

import time
start = time.time()

n = 10000
primes = find_primes_up_to_x(n)
primeSet = set(primes)
twiceSquares = [2*number**2 for number in range(1,int(n**0.5))]

for odd in range(3,n,2):
    if odd in primeSet:
        continue
    
    found = False
    smallerPrimes = [prime for prime in primeSet if prime < odd]
    
    for prime in smallerPrimes:
        if((odd - prime) in twiceSquares):
            found = True
            #print(odd, prime, odd-prime, found)
            break
    if found == False:
        print(odd)
        break

print("Running time is: ",round(time.time()-start,4), "Seconds")
#Running time is 0.69 Seconds