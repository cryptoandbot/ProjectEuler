"""
Print the 10001st prime number
"""

counter = 1
counterUp = 2
primeCounter = 2

while counter <= 10001:
    isPrime = True
    counterUp = 2
    while counterUp < (primeCounter) and isPrime == True:
        if primeCounter % counterUp == 0:
            isPrime = False
        counterUp += 1
    if isPrime == True:
        print(str(counter) + " :: " + str(primeCounter))
        counter += 1
    primeCounter += 1
