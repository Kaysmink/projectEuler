# -*- coding: utf-8 -*-
"""
Created on Fri Sep 17 10:53:00 2021

@author: kaysm
"""

import time
def one_to_nine_pandigital_9_digit(number):
    number=list(map(int,list(str(number))))
    if(len(number) != 9):
        return False
    if(all(items in number for items in [1,2,3,4,5,6,7,8,9])):
        return True
    return False    

start=time.time() 
pandigitals = []
# get all number from between 1 and 10.000 which begins with at least 91....
# because we know from the example that largest possible i bigger than 918273645
numbers = [x for x in range(1,10000) if int(str(x)[0:2]) >= 91]
for number in numbers:
    multiplier = 0
    concat = ""
    while True:
        multiplier = multiplier + 1
        mult = number * multiplier
        TestConcat = concat + str(mult)
        if(len(TestConcat) <= 9):
            concat = concat + str(mult)
        elif(len(TestConcat) > 9):
            break
        
        if(len(concat) == 9):
            break
    
    if(one_to_nine_pandigital_9_digit(int(concat))):
        pandigitals.append(int(concat))

print(sorted(pandigitals)[-1])
print("Running time is: ",round(time.time()-start,4), "Seconds")
#running time is 0.0 seconds
      
    