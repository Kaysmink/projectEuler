# -*- coding: utf-8 -*-
"""
Created on Tue Jul 23 21:23:04 2019

@author: kaysm
"""

import time

start=time.time()

Input=open("67. Maximum path sum II Input.txt","r").read().split("\n")

for i in range(0,len(Input)):
    Input[i]=list(map(int,Input[i].split(" ")))


answer_matrix=[[Input[0][0]]]
for i in range(1,len(Input)):
    answer=[]
    for j in range(0,len(Input[i])):
        if(j==0):
            position_minus_one=0
        else:
            position_minus_one=Input[i][j]+answer_matrix[i-1][j-1]
        if(j>len(Input[i-1])-1):
            position=0
        else:
            position=Input[i][j]+answer_matrix[i-1][j]         
         
        answer.append(max(position, position_minus_one))
    answer_matrix.append(answer)

print(max(answer_matrix[-1]))

print("Running time is: ",round(time.time()-start,4), "Seconds")
#Running time is 0.02 Seconds