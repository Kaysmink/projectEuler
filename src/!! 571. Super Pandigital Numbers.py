# -*- coding: utf-8 -*-
"""
Created on Tue Jul 30 14:23:59 2019

@author: kaysm
"""
import string
import time
import itertools as it

def zero_to_b_pandigital(number,b):
    number=str(number)
    for i in range(b-1,-1,-1):
        if(number.find(str(i))!=-1):
            number=number.replace(str(i), "X", 1)
        else:
            return False
    return True

"""
following function copied from :
https://stackoverflow.com/questions/2267362/how-to-convert-an-integer-in-any-base-to-a-string
"""
def int2base(x, base):
    if x < 0:
        sign = -1
    elif x == 0:
        return digs[0]
    else:
        sign = 1

    x *= sign
    digits = []

    while x:
        digits.append(digs[int(x % base)])
        x = int(x / base)

    if sign < 0:
        digits.append('-')

    digits.reverse()

    return ''.join(digits)

def is_super_pandigital(number, base):
    for j in range(base,1,-1):
        if(zero_to_b_pandigital(int2base(number, j), j)==False):
            return False
    return True


start=time.time()
digs = string.digits + string.ascii_letters

base=12
super_pandigital_numbers=[]
for perm in it.permutations(range(0,base)):
    if(perm[0]==0):
        continue    
    else:
        perm=int("".join(list(map(str,perm))))
        if(is_super_pandigital(perm,base)):
            super_pandigital_numbers.append(perm)
            print(len(super_pandigital_numbers),"Running time is: ",round(time.time()-start,4), "Seconds")
            if(len(super_pandigital_numbers)==10):
                break


print(sum(super_pandigital_numbers))
print("Running time is: ",round(time.time()-start,4), "Seconds")
#Running time is infinity
            
            
            
