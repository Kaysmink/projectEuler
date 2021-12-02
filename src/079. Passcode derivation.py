# -*- coding: utf-8 -*-
"""
Created on Mon Sep 20 11:11:37 2021

@author: kaysm
"""

import time
from collections import defaultdict

def pandigital(number, numbersNeeded):
    number=list(number)
    if(all(items in number for items in numbersNeeded)):
        return True
    return False    

starttime = time.time()

f=open("Input/79. Passcode derivation Input.txt", "r")
Input = [line.strip() for line in f]

nextNum = defaultdict(list)
for line in Input:
    for i in range(0,len(line)-1):
            nextNum[line[i]].append(line[i+1])

for key, value in nextNum.items():
    nextNum[key] = set(value)

start = "7"

possibles = [start]
while True:
    for number in possibles:
        lastDig = number[-1]
        for nextN in nextNum[lastDig]:
            new = number + nextN
            possibles.append(new)
            if pandigital(new, nextNum.keys()):
                print(new)
                break
    break

print("Running time is: ",round(time.time()-starttime,4), "Seconds")
#Running time is 0.0156 seconds