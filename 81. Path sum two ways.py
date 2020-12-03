# -*- coding: utf-8 -*-
"""
Created on Thu Jul 25 10:58:22 2019

@author: kaysm
"""

import time 

start=time.time()

matrix=open("81. Path sum two ways Input.txt","r").readlines()

for i in range(0,len(matrix)):
    matrix[i]=list(map(int,matrix[i].split(",")))
    

score_matrix=[["NA" for i in range(0,80)] for i in range(0,80)]

"most upper left value"
score_matrix[0][0]=matrix[0][0]

"First row"
for i in range(1,len(matrix[0])):
    score_matrix[0][i]=score_matrix[0][i-1]+matrix[0][i]

"First column"
for i in range(1,len(matrix[0])):
    score_matrix[i][0]=score_matrix[i-1][0]+matrix[i][0]

"Calculate minimal values for reaching all other points in the matrix" 
for i in range(1,len(matrix)):
    for j in range(1, len(matrix)):
        right=score_matrix[i][j-1]+matrix[i][j]
        down=score_matrix[i-1][j]+matrix[i][j]
        
        score_matrix[i][j]=min(right, down)

print(score_matrix[79][79])
print("Running time is: ",round(time.time()-start,4), "Seconds")
#Running time is 0.018 Seconds

    

        