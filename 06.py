"""
The sum of the squares of the first ten natural numbers is,
1^2 + 2^2 + ... + 10^2 = 385.
The square of the sum of the first ten natural numbers is,
(1 + 2 + ... + 10)^2 = 552 = 3025.
Hence the difference between the sum of the squares of the first ten natural numbers and the square of
the sum is 3025 − 385 = 2640.
Find the difference between the sum of the squares of the first one hundred natural numbers and the
square of the sum.

answer = 25164150
"""
answer = 25164150
inp = 100

sum_of_square = ((inp+1)*inp)//2
sum_of_square = sum_of_square**2

square_of_sum = (inp*(inp+1)*(2*inp+1))//6


print(sum_of_square-square_of_sum == answer)