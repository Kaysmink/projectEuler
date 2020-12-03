# -*- coding: utf-8 -*-
"""
Created on Mon Jul 22 20:21:34 2019

@author: kaysm
"""

import time

def print_matrix_on_screen(matrix, width=4):
    for row in matrix:
        print(''.join(['{0:>{w}}'.format(item, w=width) for item in row]))
  
start=time.time()      
Input=open("11. Largest product in a grid Input.txt","r")
Input=Input.readlines()

matrix=[]
Sum_matrix=[["NA" for i in range(20)] for i in range(20)]
for line in Input:
    line=list(map(int,line.split(" ")))
    matrix.append(line)

for i in range(0,len(matrix)):
    for j in range(0,len(matrix)):
        if(j>16):
            horizontal=0
        else:
            horizontal=matrix[i][j]*matrix[i][j+1]*matrix[i][j+2]*matrix[i][j+3]
        if(i>16):
            vertical=0
        else:
            vertical=matrix[i][j]*matrix[i+1][j]*matrix[i+2][j]*matrix[i+3][j]
        if(i>16 or j>16):
            diagonal_down=0
        else:
             diagonal_down=matrix[i][j]*matrix[i+1][j+1]*matrix[i+2][j+2]*matrix[i+3][j+3]
        if(i<4 or j>16):
            diagonal_up=0
        else:
             diagonal_up=matrix[i][j]*matrix[i-1][j+1]*matrix[i-2][j+2]*matrix[i-3][j+3]
        value=max(horizontal, vertical, diagonal_up, diagonal_down)  
        Sum_matrix[i][j]=value
        
max_values=[max(line) for line in Sum_matrix]
print(max(max_values))
print("Running time is: ",round(time.time()-start,4), "Seconds")
#Running time is 0.004 seconds




