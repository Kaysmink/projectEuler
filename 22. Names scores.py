# -*- coding: utf-8 -*-
"""
Created on Thu Jul 18 17:55:46 2019

@author: kaysm
"""

import time

def Euler22(filename='22. Names scores Input.txt'):
    import string                                                #De data inlezen
    data = open(filename)
    names= [word.strip() for line in data.readlines() for word in line.split(',') if word.strip()]
    names=sorted(names)
    numberOfNames=len(names)
    som=0
    
    Letters = list(string.ascii_uppercase)
    LettersValues=[i for i in range(1,27)]
    
    for i in range(numberOfNames):
        sumOfWord=0
        wordLength=len(names[i])
        for j in range(wordLength):
            if names[i][j]=="":
                sumOfWord=sumOfWord+0  
            else:
                for k in range(len(Letters)):
                    if names[i][j] == Letters[k]:
                        sumOfWord=sumOfWord+LettersValues[k]
        sumOfWord=sumOfWord*(i+1)            
        som= som+sumOfWord    
    
    print("the total of all the name scores in the file is {}".format(som)) 

start=time.time()

Euler22()

print("Running time is: ",round(time.time()-start,4), "Seconds")
#Running time is 0.26 Seconds