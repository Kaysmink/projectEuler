# -*- coding: utf-8 -*-
"""
Created on Sat Oct  2 13:46:12 2021

@author: kaysm
"""

import time 
import itertools as it

start=time.time()

def GetSequences(n):
    Triangle = [int((i*(i+1))/2) for i in range(1,n+1)]
    Square = [int(i**2) for i in range(1,n+1)]
    Pentagonal = [int(i*(3*i-1)/2) for i in range(1,n+1)]
    Hexagonal = [int(i*(2*i-1)) for i in range(1,n+1)]
    Heptagonal = [int((i*(5*i-3))/2) for i in range(1,n+1)]
    Octagonal = [int((i*(3*i-2))) for i in range(1,n+1)]
    
    result = [Triangle, Square, Pentagonal, Hexagonal, Heptagonal, Octagonal]
    result = [[number for number in List if len(str(number)) <= 4] for List in result]
    return result

sequences = GetSequences(150)
sequences_4Digits = result = [[number for number in List if len(str(number)) == 4] for List in sequences]

possibilities = []
for value1 in sequences_4Digits[0]:
    for comb in it.permutations(range(1,6), 5):
        comb = list(comb)
        possVal2 = [number for number in sequences_4Digits[comb[0]] if str(number).startswith(str(value1)[-2:])]
        if len(possVal2) == 0:
            continue
        for value2 in possVal2:
            possVal3 = [number for number in sequences_4Digits[comb[1]] if str(number).startswith(str(value2)[-2:])]
            if len(possVal3) == 0:
                continue
            for value3 in possVal3:
                possVal4 = [number for number in sequences_4Digits[comb[2]] if str(number).startswith(str(value3)[-2:])]
                if len(possVal4) == 0:
                    continue
                for value4 in possVal4:
                    possVal5 = [number for number in sequences_4Digits[comb[3]] if str(number).startswith(str(value4)[-2:])]
                    if len(possVal5) == 0:
                        continue
                    for value5 in possVal5:
                        possVal6 = [number for number in sequences_4Digits[comb[4]] if str(number).startswith(str(value5)[-2:])]
                        if len(possVal6) == 0:
                            continue
                        for value6 in possVal6:
                            possibilities.append([value1, value2, value3, value4, value5, value6])

result = [poss for poss in possibilities if str(poss[0])[0:2] == str(poss[5])[-2:]]
print(sum(result[0]))

print("Running time is: ",round(time.time()-start,4), "Seconds")
#Running time is 1.5716 seconds



1504170715041707*2%4503599627370517


