"""
Find the sum of all multiples of 3 or 5 below 1000.
"""

multiple_list = []
for x in range(1000):
    v = 3 * x
    if v < 1000:
        multiple_list.append(v)
    else:
        break

for y in range(1000):
    u = 5 * y
    if u < 1000:
        if u % 3 != 0:
            multiple_list.append(u)
    else:
        break

print (sum(multiple_list))
