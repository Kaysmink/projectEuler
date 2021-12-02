# -*- coding: utf-8 -*-
"""
Created on Sat Jul 20 19:21:38 2019

@author: kaysm
"""
import time

start=time.time()

circular_primes=[2]
limit=1000000

def is_prime(number):
    for j in range(2,int(number**0.5+1)):
        if(number%j==0):
            return False
    return True

def rotations(n):
    answer = []
    rotation = str(n)
    while not rotation in answer:
        answer.append(rotation)
        rotation = rotation[1:] + rotation[0]
    return list(map(int,answer))

def is_circular(number):
    permutations=rotations(number)
    for value in permutations:
        if(is_prime(value)==False):
            return False
    return True      

for i in range(3,limit,2):
    if(is_prime(i)):
        print(i)
        if(is_circular(i)):
            circular_primes.append(i)
            
print(len(circular_primes))
print("Running time is: ",round(time.time()-start,4), "Seconds")
#Running time is 21.58 Seconds
        
        
    
