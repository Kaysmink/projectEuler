# -*- coding: utf-8 -*-
"""
Created on Mon Jul 22 14:49:01 2019

@author: kaysm
"""
import time 

start=time.time()

words=open("42. Coded triangle numbers Input.txt", "r").read().replace('"',"").split(",")

number_of_words=[]

def is_triangle(number):
    return

def make_list_of_triangle_numbers(Max):
    i=1
    value=0
    triangle_numbers=[]
    while(value<Max):
        value=(int(0.5*i*(i+1)))
        triangle_numbers.append(value)
        i=i+1
    return triangle_numbers
        
for word in words:
    Sum=0
    for char in word:
        Sum=Sum+ord(char.lower())-96
    number_of_words.append(Sum)

max_number=max(number_of_words)
triangle_numbers=make_list_of_triangle_numbers(max_number)
print(sum(value in triangle_numbers for value in number_of_words))

print("Running time is: ",round(time.time()-start,4), "Seconds")
#Running time is 0.01 Seconds



