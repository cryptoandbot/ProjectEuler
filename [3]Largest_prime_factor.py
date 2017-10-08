"""
Find the largest prime factor of 600851475143
"""

f = 600851475143

counterUp = 2
counterDown = 2
largestPrime = 0

while counterUp < f and largestPrime == 0:
    if f % counterUp == 0:
        factor = f / counterUp
        isPrime = True
        counterDown = 2
        while counterDown < factor and isPrime == True:
            if factor % counterDown == 0:
                isPrime = False
            counterDown += 1
        if largestPrime == 0 and isPrime == True:
            largestPrime = factor
    counterUp += 1

print (largestPrime)
