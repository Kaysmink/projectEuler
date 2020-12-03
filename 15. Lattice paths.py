# -*- coding: utf-8 -*-
"""
Created on Thu Jul 18 13:42:35 2019

@author: kaysm
"""
import time

def print_matrix_on_screen(matrix, width=4):
    for row in matrix:
        print(''.join(['{0:>{w}}'.format(item, w=width) for item in row]))

start=time.time()
dimension=20
matrix=[["NA"] * dimension for i in range(dimension)]
matrix[0]=[1]*dimension
matrix[0][0]=0

for i in range(1,dimension):
    matrix[i][0]=1

for i in range(1,dimension):
    for j in range(1,dimension):
        matrix[i][j]=matrix[i-1][j]+matrix[i][j-1]
        
print_matrix_on_screen(matrix)

print("\nAnswer is: ",matrix[dimension-1][dimension-1])
print("Running time is: ",round(time.time()-start,4), "Seconds")
#Running time is 0.01 Seconds











