# -*- coding: utf-8 -*-
"""
Created on Sat Aug  3 21:29:41 2019

@author: kaysm
"""

import time


def is_prime(number):
    if(number==1 or number ==0):
        return False
    if(number%2 == 0 and number > 2):
        return False
    for i in range(3,int(number**0.5+1), 2):
        if(number%i==0):
            return False
    return True

def find_primes_up_to_x_old(x):    
    prime_list=[2]
    prime_list_visited=["NA" for i in range(0,x+1)]
    for i in range(3,len(prime_list_visited),2):
        if(i%2==0):
            prime_list_visited[i]=True
            continue
        if(prime_list_visited[i]==True):
            continue
        else:
            if(is_prime(i)==False):
                prime_list_visited[i]=True
            else:
                prime_list_visited[i]=True
                prime_list.append(i)
            multiplier=2
            while(i*multiplier<=x):
                prime_list_visited[i*multiplier]=True
                multiplier=multiplier+1
    return prime_list 

def find_primes_up_to_x(x):
    odds = [i for i in range(3, x+1,2)] 
    primes = ["prime" for i in range(0,x+1)]
    primes[1] = "NA"
    for even in range(0,x+1,2):
        primes[even] = "NA"
    primes[2] = "prime"
    for number in odds:
        if(number**0.5 > x):
            break
        if(primes[number] != "prime"):
            continue
        else:
            multiplier = 2
            while(number * multiplier < x):
                multiplication = number * multiplier
                primes[multiplication] = "NA"
                multiplier = multiplier + 1
    primes = [prime for prime, boolean in enumerate(primes) if boolean == "prime"]
    return primes

#start = time.time()    
#test = find_primes_up_to_x(10000000)
#print("time version 1: ",time.time() - start)

#start = time.time()
#testen = find_primes_up_to_x(10000000)
#print("time version 2: ", time.time() - start)
