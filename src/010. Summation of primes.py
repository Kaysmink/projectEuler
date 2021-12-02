# -*- coding: utf-8 -*-
"""
Created on Wed Jul 17 21:19:25 2019

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

def find_primes_up_to_x(x):    
    prime_list=[2]
    prime_list_visited=["NA" for i in range(0,x+1)]
    for i in range(3,len(prime_list_visited),2):
        if(i%2==0):
            prime_list_visited[i]==True
        elif(prime_list_visited[i]!="NA"):
            continue
        else:
            if(is_prime(i)==False):
                prime_list_visited[i]==True
                multiplier=2
                while(i*multiplier<=x):
                    prime_list_visited[i*multiplier]==True
                    multiplier=multiplier+1
            else:
                prime_list_visited[i]==True
                prime_list.append(i)
                multiplier=2
                while(i*multiplier<=x):
                    prime_list_visited[i*multiplier]==True
                    multiplier=multiplier+1
    return prime_list 

start=time.time()
answer=sum(find_primes_up_to_x(2000000))
print(answer) 
print("Running time of algortihm is:", round(time.time()-start,4), "Seconds")                    
#Running time is 21.58 Seconds

             