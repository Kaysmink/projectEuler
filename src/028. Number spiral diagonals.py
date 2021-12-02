# -*- coding: utf-8 -*-
"""
Created on Fri Jul 19 20:54:47 2019

@author: kaysm
"""
import time

start=time.time()

dimension=1001
Sum=0
for i in range(1,dimension+1,2):
    Sum=Sum+i**2

bottum_r_start=1
bottum_l_start=1
top_l_start=1
bottum_r_diff=2
bottum_l_diff=4
top_l_diff=6

for i in range(1,dimension,2):
    new=bottum_r_start+bottum_r_diff
    Sum=Sum+new
    bottum_r_start=new
    bottum_r_diff=bottum_r_diff+8
    
    new=bottum_l_start+bottum_l_diff
    Sum=Sum+new
    bottum_l_start=new
    bottum_l_diff=bottum_l_diff+8
    
    new=top_l_start+top_l_diff
    Sum=Sum+new
    top_l_start=new
    top_l_diff=top_l_diff+8
    
print("Sum of Diagonals is ", Sum)

print("Running time is: ",round(time.time()-start,4), "Seconds")
#Running time is 0.003 Seconds
    