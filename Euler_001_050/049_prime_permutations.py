from sympy import primerange, isprime
from itertools import permutations

#Input : Integer N (assumed with 4 digits)
#Output : list of prime greater than 1000 that are of permutations of N
def list_permutations(N):
    list_prime_permutation = set()
    for digits in permutations(str(N)):
        permutation = int(''.join(digits))
        if isprime(permutation) and permutation>1000:
            list_prime_permutation.add(permutation)
    return sorted(list_prime_permutation)

#For a given list of number (assumed sorted) we ant to see if there is an arithmetic sequence.
#Having the first two terms of the sequence, we can calculate the third one:
# a, b, b+b-a
#So for each couple of numbers we look if the third number of the potential sequnce is in the list.
def is_arithmetic_serie(serie):
    for i in range(len(serie)-1):
        for j in range(i+1,len(serie)):
            if 2*serie[j]-serie[i] in serie:
                print(serie[i])
                print(serie[j])
                print(2*serie[j]-serie[i])


#For each prime with 4-digits, we return the list of prime that are a permutation of the first one
#Of course two prime that are a permution of each other will generate the same lis.
#I decided to filter after the list creations, because there is about 1000 prime between 1000 and 10000

prime_4_digits = list(primerange(1000, 10000))
possible_sequence = []
for prime in prime_4_digits:
    if len(list_permutations(prime))>2:
        if list_permutations(prime) not in possible_sequence:
            possible_sequence.append(list_permutations(prime))

for serie in possible_sequence:
    is_arithmetic_serie(serie)


