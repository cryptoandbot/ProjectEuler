"""
Sum of even Fibonacci numbers below 4,000,000
"""

def fib(x):
    even_fib_list = []
    a = 0
    b = 1
    n = 0
    while n < x:
        n = a + b
        if n % 2 == 0:
            even_fib_list.append(n)
        if a < b:
            a = n
        else:
            b = n
    return sum(even_fib_list)

print (fib(4000000))
