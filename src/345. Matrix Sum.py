# -*- coding: utf-8 -*-
"""
Created on Wed Sep 29 19:04:48 2021

@author: kaysm
"""

import itertools as it
import time 

start = time.time()

with open("Input/345. Matrix Sum Input.txt", 'r') as f:
    matrix = [[int(num) for num in line.split()] for line in f]


maxSum = 0
for comb in it.permutations(range(len(matrix)), len(matrix)):
    Sum = 0 
    comb = list(comb)
    for y, x in enumerate(comb):
        Sum = Sum + matrix[y][x]
    
    if Sum > maxSum:
        maxSum = Sum

print(maxSum)

print("Running time is: ",round(time.time()-start,4), "Seconds")
#Running time is 0.31 Seconds      