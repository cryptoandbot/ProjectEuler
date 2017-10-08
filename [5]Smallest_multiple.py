"""
Find the smallest even positive number that is evenly divisible (no remainder) by all the numbers from 1 to 20
"""

def create_num_list(limit):
    num_list = []
    for a in range(1, limit+1):
        num_list.append(a)
    return num_list

num_list = create_num_list(20)

end = False
s = 20


while end == False:
    viable = False
    for x in num_list:
        if s % x == 0:
            viable = True
        else:
            viable = False
            break
    if viable == True:
        end = True
    else:
        s = s + 20

print (s)
