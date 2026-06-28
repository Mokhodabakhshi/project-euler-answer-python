"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any
remainder.
What is the smallest positive number that is evenly divisible2 by all of the numbers from 1 to 20?
"""

import math

a = 20

def is_prime(x):
    for i in range(2,int(math.sqrt(x))+1):
        if x % i == 0:
            return False
    return True

prime = []
for i in range(2,a+1):
    if is_prime(i):
        prime.append(i)

res = []
for val in prime:
    p = 1
    temp = val
    while True:
        temp *= val
        if temp > a:
            print(f"{val}^{p}")
            res.append(temp)
            break
        p += 1
   
for i in range(len(prime)):
    res[i] = res[i]//prime[i]

mul = 1
for i in res:
    mul *= i
print(mul)
