#Notice 1: with n = 0 we see that b as to be a prime.
#Notice 2: with n = b we see that n^2 + an+b = b(b+a+1) is composite. So we can be sure that the formula will not
#create an infinite number of prime.

from sympy import primerange, isprime

#Return the list of possible value for b (or the list of prime numbers lesser than 1000 and their opposite.
def prime_lesser_than(N):
    list_prime_neg_pos = []
    for i in primerange(N+1):
        list_prime_neg_pos.append(i)
        list_prime_neg_pos.append(-i)
    return list_prime_neg_pos

#for a given b, thsi function return a that produces the longest serie of prime, and the number of consecutives prime.
#At first, a can take any value from -1000 to 1000
# for each value of n, we look at the value of a that make n*n+n*a+b a prime number and we keep only these values
# we reduce the list until we have no more available values.
#We have at maximum b passage in the loop (Notice 2)

def best_a_value(b):
    a_value= list(range(-1000,1001,1))
    n = 1
    while len(a_value) !=0:
        temp = [a for a in a_value]
        for a in a_value:
            if not isprime(n*n+n*a+b) and not isprime(-n*n-n*a-b):
                temp.remove(a)
        if len(temp) == 0:
            best_value = a_value[0]
        a_value = temp
        n +=1
    return n-1, best_value


# for each value of b, we look at the optimal a, and we compare with the last found couple
def main():
    b_value = prime_lesser_than(1000)
    b_max = 0
    a_max = 0
    consecutive_max = 0
    for b in b_value:
        length, a = best_a_value(b)
        if length > consecutive_max:
            b_max = b
            a_max = a
            consecutive_max = length

    print(a_max*b_max)

main()








