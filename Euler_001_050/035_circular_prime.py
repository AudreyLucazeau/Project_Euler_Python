'''
Notice 1 :
if the number contains a 5 (but 5 itself) will not be a circular prime.
indeed, every integer than end by a five is divisible by 5.

Notice 2 :
if the number contains a even number (but 2 itself) will not be a circular prime.
indeed, every integer than end by an even number is divisible by 2.

CCL: number are composed only by 1, 3, 7, and 9 (but 2 and 5 itself)

If we exclude number lesser than 10
We have 4^2+4^3+4^4+4^5+4^6 = 5456 values to test

A more optimal approach could be imagined to avoid testing separately the number that belongs to the same circular cycle
But looking at the low number of number to try, we can easily try every number
'''

from sympy import isprime

def circular(N):
    return int(str(N)[1:]+str(N)[0])


def circular_prime_100_999():
    count_circular_prime=0
    for a in [1,3,7,9]:
        for b in [1,3,7,9]:
            for c in [1,3,7,9]:
                number = 100*c+10*b+a
                if is_circular_prime(number):
                    count_circular_prime += 1
    return count_circular_prime

def circular_prime_1000_9999():
    count_circular_prime=0
    for a in [1,3,7,9]:
        for b in [1,3,7,9]:
            for c in [1,3,7,9]:
                for d in [1,3,7,9]:
                    number = 1000*d+100*c+10*b+a
                    if is_circular_prime(number):
                        count_circular_prime += 1
    return count_circular_prime

def circular_prime_10000_99999():
    count_circular_prime=0
    for a in [1,3,7,9]:
        for b in [1,3,7,9]:
            for c in [1,3,7,9]:
                for d in [1, 3, 7, 9]:
                    for e in [1, 3, 7, 9]:
                        number = 10000*e + 1000 * d + 100 * c + 10 * b + a
                        if is_circular_prime(number):
                            count_circular_prime += 1
    return count_circular_prime

def circular_prime_100000_999999():
    count_circular_prime=0
    for a in [1,3,7,9]:
        for b in [1,3,7,9]:
            for c in [1,3,7,9]:
                for d in [1, 3, 7, 9]:
                    for e in [1, 3, 7, 9]:
                        for f in [1, 3, 7, 9]:
                            number = 100000*f + 10000*e + 1000 * d + 100 * c + 10 * b + a
                            if is_circular_prime(number):
                                count_circular_prime += 1
    return count_circular_prime

def is_circular_prime(N):
    for _ in range(len(str(N))):
        if not isprime(N):
            return False
        N = circular(N)
    return True

print(circular_prime_100_999()+circular_prime_1000_9999()+circular_prime_10000_99999()+circular_prime_100000_999999()+13)






