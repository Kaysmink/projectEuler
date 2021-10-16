# -*- coding: utf-8 -*-
"""
Created on Fri Jul 19 16:57:28 2019

@author: kaysm
"""
import time

start=time.time()

abondent=[]
deficient=[]
perfect=[]
for i in range(0,28123+1):
    devisors=[]
    for j in range(1,int(i/2)+1):
        if(i%j==0):
            devisors.append(j)
    if(sum(devisors)>i):
        abondent.append(i)
    if(sum(devisors)<i):
        deficient.append(i)
    if(sum(devisors)==i):
        perfect.append(i)

allSums={}
for i in range(0,len(abondent)):
    for j in range(0,len(abondent)):
        allSums[abondent[i]+abondent[j]]=True

results=[i for i in range(0,28123+1) if(i not in allSums.keys())]
print(sum(results))

print("Running time is: ",round(time.time()-start,4), "Seconds")
#Running time is 83.97 Seconds






       
    