#first part, check is a number is a palyndrom

from math import sqrt

def is_palyndrom(N):
    N_reversed = int(str(N)[::-1])
    if N == N_reversed:
        return True
    return False
'''
We need the largest palyndrom that can be written
 a*n where 100<a<999 and 100<b<999
 For each value of a, we will look at the greatest value of b in such a way a*b is a palyndrom.
 To don't repeat calculations we can assume a>b
 With this asusmption, when we find a palyndrom we can have a lower limit for a.
 
 Indeed if a1*b1 =N is a palyndrom
 If a<sqrt(N) all the product a*b<a*a<N
'''

def largest_palyndrom():
    a = 1000
    max_palyndrom = 0
    limit_a = 0
    while a>limit_a:
        b=a
        while not is_palyndrom(a*b) and b>0:
            b=b-1
        if a*b > max_palyndrom:
            max_palyndrom = a*b
            limit_a = round(sqrt(max_palyndrom),0)
        a -= 1
    print(max_palyndrom)

largest_palyndrom()