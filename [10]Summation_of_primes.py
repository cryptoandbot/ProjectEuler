"""
Find the sum of all primes below 2 million
"""

counter = 2
counterUp = 2
summation = 0

while counter < 2000000:
    
    counterUp = 2
    isPrime = True

    while counterUp < counter:
        if counter % counterUp == 0:
            isPrime = False
        counterUp += 1

    if isPrime == True:
        summation += counter

    counter += 1

print (summation)
