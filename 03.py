"""
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143?
"""

from math import sqrt

n = 600851475143
def is_prime(x):
    for i in range(2,int(sqrt(x))+1):
        if x % i == 0:
            return False
    return True

temp = []
for i in range(2,int(sqrt(n))+1):
    if is_prime(i) and not(n % i):
        temp.append(i)
        n /= i

print(max(temp))

