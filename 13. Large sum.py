# -*- coding: utf-8 -*-
"""
Created on Thu Jul 18 13:16:23 2019

@author: kaysm
"""
import time

start=time.time()
Input=open("13. Large sum Input.txt", "r")
Input=list(map(float,Input.read().split("\n")))

Sum=str(int((sum(Input))))
answer=Sum[0:10]
print(answer)
print("Running time is: ",round(time.time()-start,4), "Seconds")
#Running time is 0.002 seconds