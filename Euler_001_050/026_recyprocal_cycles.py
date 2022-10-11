
#Documentation :
#https://en.wikipedia.org/wiki/Repeating_decimal

#digit_recurring(D) return the length of the recurring cycle of 1/D
#Reciprocals of integer not coprime to 10 (that we can write D = 2^a * 5^b *K with k coprime to 10)
# as the same length of recurring pattern than 1/K.
#If K is coprime to 10, we can express 1/K = M/(10^d -1)
# The smallest possible D is the length of the recurring cycle.



def digit_recurring(D):

    while  D %2 == 0:
        D //= 2
    while  D %5 == 0:
        D //= 5
    if D == 1:
        return 0

    #Now D is not divisible by 2 or 5, D is coprime to 10
    i=1

    #Note : this loop will end because, as D is coprime to 10, according
    #to the Fermat's little theorem 10^D-1 % D == 1.
    while (10**i) % D != 1:
        i += 1
    return i

def main():
    length_max = 0
    denominator_max = 1
    for d in range(1,1000):
        if digit_recurring(d) > length_max:
            length_max = digit_recurring(d)
            denominator_max = d
    return denominator_max

print(main())
