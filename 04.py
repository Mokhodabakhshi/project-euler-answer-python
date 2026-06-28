"""
A palindromic number reads the same both ways. The largest palindrome made from the product of two
2-digit numbers is 9009 = 91 × 99.
Find the largest palindrome made from the product of two 3-digit numbers.
"""

n = 1000
res = []
for i in range(n//10,n):
    for j in range(n//10,n):
        s = i*j
        str_s = str(s)
        if str_s == str_s[::-1]:
            res.append(s)

print(max(res))