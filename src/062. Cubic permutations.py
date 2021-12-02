# -*- coding: utf-8 -*-
"""
Created on Mon Sep 20 12:49:36 2021

@author: kaysm
"""

import time
from collections import Counter

start = time.time()

cubes = [cube**3 for cube in range(1, 10000) if len(str(cube**3)) > 5]
sortedCubes = ["".join(sorted(str(cube))) for cube in cubes]
counter = Counter(sortedCubes)

perm5 = min([cube for cube in cubes if counter["".join(sorted(str(cube)))] == 5])
print(perm5)

print("Running time is: ",round(time.time()-start,4), "Seconds")
#Running time is 0.0468 seconds