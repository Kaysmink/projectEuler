# -*- coding: utf-8 -*-
"""
Created on Wed Jul 17 20:58:09 2019

@author: kaysm
"""

import time 

def Euler4(digits=3):
    def isPalindrome(n):
        reverse=0
        number=n
        while n>0:
            reverse = reverse*10 + n % 10
            n=n//10
        if reverse==number:
            return True
    
    largestNumber=0
    number1=0
    number2=0
    for i in range(10**(digits-1),10**digits):
        for j in range(10**(digits-1),10**digits):
            number=i*j
            if isPalindrome(number)==True:
                if number>largestNumber:
                    largestNumber=number
                    number1=i
                    number2=j
    print("\nThe largest palindrome is {}".format(largestNumber))
    print("with factors {} and {}\n".format(number1,number2))            

start=time.time()
Euler4()
print("Running time is: ",round(time.time()-start,4), "Seconds")
#Running time is 1.96 seconds