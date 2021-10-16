# -*- coding: utf-8 -*-
"""
Created on Mon Jul 22 12:55:15 2019

@author: kaysm
"""
import time

def is_prime(number):
    if(number==1):
        return False
    for j in range(2,int(number**0.5+1)):
        if(number%j==0):
            return False
    return True

def rotations(n):
    answer = []
    value1 = str(n)
    value2 = str(n)
    while(len(value1)>1 and len(value2)>1):
        value1=value1[1:]
        value2=value2[:len(value2)-1]        
        answer.append(value1)
        answer.append(value2)
    return(list(map(int,answer)))

def is_truncatable(number):
    permutations=rotations(number)
    for value in permutations:
        if(is_prime(value)==False):
            return False
    return True  

start=time.time()
truncatable=[]
i=11
while(len(truncatable)<11):
    if(is_prime(i)):
        if(is_truncatable(i)):
            truncatable.append(i)
    i=i+2
    
print(sum(truncatable))

print("Running time is: ",round(time.time()-start,4), "Seconds")
#Running time is 8.32 Seconds
    


    
    
    
    
    
    