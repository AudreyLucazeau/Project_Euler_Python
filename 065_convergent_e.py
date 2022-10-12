from fractions import Fraction as frac

#input : a term in the sequence of convergents of e, and the equivqlent term in the simple continued fraction representaiton
#output : the next term in the sequence of convergents of e.
def next_fraction(previous_fraction : frac, k):
    return k+1/previous_fraction

def fraction_of_e(n):

    #Generate the n first terms of the simple continued fraction representations of e
    continuous_fraction_e=[1]*n
    continuous_fraction_e[0]=2
    for i in range(2,n,3):
        continuous_fraction_e[i]= 2*(i//3+1)


    fraction_e = frac(continuous_fraction_e[-1],1)
    for j in range(1,n):
        fraction_e = next_fraction(fraction_e, continuous_fraction_e[n-1-j])

    return fraction_e

print(fraction_of_e(100))
n_step = sum([int(i) for i in str(fraction_of_e(100).numerator)])

print(n_step)




