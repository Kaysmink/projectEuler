# -*- coding: utf-8 -*-
"""
Created on Thu Aug  8 22:17:37 2019

@author: kaysm
"""

import time
from src.hulpfuncties.Find_primes_up_to_x import *

start=time.time()

def GetTriangle(n):
    oldLine =[1,1]
    distinctNumbers = set(oldLine)
    for i in range(2, n):
        newLine = [oldLine[x-1] + oldLine[x] for x in range(1,len(oldLine))]
        newLine = [1] + newLine + [1]
        distinctNumbers.update(newLine)  
        oldLine = newLine
    
    return distinctNumbers

def IsSquareFree(number, primesSquared):
    possibleSquares = [square for square in primesSquared if square <= number]
    devisible = any([number%square == 0 for square in possibleSquares])
    
    return devisible == False


distinctNumbers = GetTriangle(51)
neededPrimes = find_primes_up_to_x(int(max(distinctNumbers)**0.5))
primesSquared = [prime**2 for prime in neededPrimes]

squareFreeNumbers = []
for number in distinctNumbers:
    if IsSquareFree(number, primesSquared):
        squareFreeNumbers.append(number)
        
print(sum(squareFreeNumbers))

print("Running time is: ",round(time.time()-start,4), "Seconds")
#Running time is 60.1 seconds