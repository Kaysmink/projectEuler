from src.hulpfuncties.Find_primes_up_to_x import *

import time
start = time.time()
primes = find_primes_up_to_x(1000000)


possibleAnswers = []
for i in range(len(primes)-150, len(primes)-200, -1):
    for j in range(0,i-22):
        Sum = 0
        x = j
        numOfPrimes = 0
        while Sum < primes[i]:
            Sum = Sum + primes[x]
            numOfPrimes = numOfPrimes + 1
            if Sum == primes[i]:
                possibleAnswers.append([primes[i], numOfPrimes])
                break
            x = x + 1
            
print(max(possibleAnswers, key=lambda x:x[1]))     
print("Running time is: ",round(time.time()-start,4), "Seconds")
#Running time is 28.42 Seconds