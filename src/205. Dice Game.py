# -*- coding: utf-8 -*-
"""
Created on Fri Sep 24 14:38:43 2021

@author: kaysm
"""

import time
import itertools as it
from collections import defaultdict 

start = time.time()

pyrPos = defaultdict(int)
cubPos = defaultdict(int)

for comb in it.product(range(1, 5), repeat = 9):
     pyrPos[sum(comb)] +=1
    
for comb in it.product(range(1, 7), repeat = 6):
     cubPos[sum(comb)] +=1
    
totalPyr = sum(pyrPos.values())
totalCub = sum(cubPos.values())
maxPyr = max(pyrPos.keys())
maxCub = max(cubPos.keys())

pyrChances = [pyrPos[i] / totalPyr for i in range(0, maxPyr+1)]
cubChances = [cubPos[i] / totalCub for i in range(0, maxCub+1)]

chancePyrWin = 0
for throw, chance in enumerate(pyrChances):
    chanceOfWin = chance * sum(cubChances[0:throw])
    chancePyrWin = chancePyrWin + chanceOfWin
    
print(chancePyrWin)
print("Running time is: ",round(time.time()-start,4), "Seconds")
#Running time is 0.1855 seconds