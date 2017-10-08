"""
Find the difference between the sum of the squares of the first 100 natural numbers and the square of the sum
"""

def sum_of_squares(n):
    counter = 1
    sqSum = 0
    while counter <= n:
        sqSum += counter*counter
        counter += 1
    return sqSum

def square_of_sum(n):
    return n*n

print(sum_of_squares(100)-square_of_sum(100))
