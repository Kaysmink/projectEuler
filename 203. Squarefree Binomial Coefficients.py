# -*- coding: utf-8 -*-
"""
Created on Thu Aug  8 22:17:37 2019

@author: kaysm
"""

import time

start=time.time()

Input=open("203. Squarefree Binomial Coefficients Input.txt","r").readlines()

triangle=[]
distinct_numbers=set([1, 2, 3, 4, 5, 6, 7, 10, 15, 20, 21, 35])
for lines in Input:
    line=lines.strip().split("\t\t")
    triangle.append(list(map(int,line)))
    
for i in range(8, 51):
    line=["NA" for i in range(0,len(triangle[i-1])+1)]
    line[0]=1
    line[len(line)-1]=1
    for j in range(1,len(line)-1):
        line[j]=triangle[i-1][j-1]+triangle[i-1][j]
        distinct_numbers.add(line[j])
    triangle.append(line)
    
distinct_numbers=list(distinct_numbers)

print("Running time is: ",round(time.time()-start,4), "Seconds")
#Running time is 0.02 Seconds