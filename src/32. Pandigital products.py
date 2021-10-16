# -*- coding: utf-8 -*-
"""
Created on Tue Jul 30 19:51:42 2019

@author: kaysm
"""

import time

def is_pandigital(number):
    n=len(number)
    if("0" in number):
        return False
    max_number=int(max(number))
    length=len((set(number)))
    if(length==max_number==n):
        return True
    return False

start=time.time()
products=[]

for i in range(100,10000):
    for j in range(1,100):
        numbers=list(str(i))
        product=i*j
        numbers=numbers+list(str(j))+list(str(product))
        if(len(numbers)>9):
            break
        if(len(numbers)==9):
            if(is_pandigital(numbers)):
                products.append(product)            

print(sum(list(set(products))))
print("Running time is: ",round(time.time()-start,4), "Seconds")
#Running time is 0.18 Seconds