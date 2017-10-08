"""
Find the pythagorean triplet where a + b + c = 1000 and show its product
Pythagorean triple is a < b < c where a^2 + b^2 = c^2
"""

a = 1

while a < 1000:
    b = 1
    while b < (1000):
        c = 1
        while c < (1000):
            #print(str(a) + " " + str(b) + " " + str(c))
            if a + b + c == 1000:
                if a < b and b < c:
                    if a*a + b*b == c*c:
                        print(a*b*c)
            c += 1
        b += 1
    a += 1
