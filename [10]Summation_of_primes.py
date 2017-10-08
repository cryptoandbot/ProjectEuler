"""
Find the sum of all primes below 2 million
"""

from math import sqrt
from itertools import count, islice

counter = 2
summation = 0

def is_prime(n):
    return n > 1 and all(n%i for i in islice(count(2), int(sqrt(n)-1)))

while counter < 2000000:
    if is_prime(counter):
        summation += counter

    counter += 1

print (summation)
