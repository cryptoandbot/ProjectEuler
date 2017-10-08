"""
Find the largest palindrome that is the product of two three digit numbers.
"""

#Creating a prime list until 999 to see if palindrome is divisible by them

prime_list = [2]
is_prime = False

for x in range(2, 999):
    for y in prime_list:
        if x % y == 0:
            is_prime = False
            break
        else:
            is_prime = True
    if is_prime == True:
        prime_list.append(x)
        is_prime = False

largest = 999 * 999
end = 0

for v in range(0,largest):
    n = largest - v
    digits = len(str(n))
    #Different action if even of odd digits
    if digits % 2 == 0:
        counter = int(digits / 2)
    else:
        counter = int((digits - 1) / 2)
    for d in range(0,counter):
        if int(str(n)[d]) == int(str(n)[digits-d-1]):
            pal = True
        else:
            pal = False
            break
    if pal == True:
        for a in range(0,999):
            b = 999 - a
            if n % b == 0 and len(str(int(n / b))) == 3 and len(str(b)) == 3:
                end = 1
                break
    else:
        pal = False
    if end == 1:
        print (n)
        print (b)
        print (n / b)
        break
