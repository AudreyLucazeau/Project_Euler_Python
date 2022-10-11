#Question :
#The prime factors of 13195 are 5, 7, 13 and 29.

#What is the largest prime factor of the number 600851475143 ?

# I made a program to find the prime decomposition of a number N
#Assumption : N is a strictly positive integer

#While N is divisible by 2, I divide it by 2.
#Then I increases by divisor (2) by one,
#While N is divisible by 3, I divide it by 3.
#Then I increases by divisor (now 3) by one,
#While N is divisible by 4, I divide it by 4.
#You can see that because N is not divisible by 2 anymore it will not be divisible by 4.
# But I choose a more brut approach.
# At least, by eliminate all predecent possible factors, I am sure, that I will obtain a decompostion in prime factors only.
# I repeat until N == 1

def decomposition_prime_factor(N):
    prime_factor = []
    factor = 2
    while N>1:
        while N%factor == 0 :
            N = N //factor
            prime_factor.append(factor)
            print(N)
        factor += 1

    return prime_factor
print(decomposition_prime_factor(600851475143))

