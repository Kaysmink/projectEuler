# -*- coding: utf-8 -*-
"""
Created on Mon Jul 22 21:45:06 2019

@author: kaysm
"""

import datetime
import time

start_time=time.time()

num_of_sundays=0
start=datetime.date(1901,1,1)
end=datetime.date(2000,12,31)
counter=(end-start).days + 1

for date in (start + datetime.timedelta(n) for n in range(counter)):
    if(date.weekday()==6 and date.day==1):
        num_of_sundays=num_of_sundays+1
print(num_of_sundays)        
    
print("Running time is: ",round(time.time()-start_time,4), "Seconds")
#Running time is 0.06 Seconds
