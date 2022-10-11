""" QUESTION :

If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000."""

# Solution 1 : Brut Force, we made a loop on all number below 1000, and for each one look if it is divisible by 3 or 5:
# To test the divisibility, we use the operator modulo
def brut_force():
    sum_multiple_3_5 = 0
    for i in range(1000):
        if i % 3 == 0 or i%5 == 0:
            sum_multiple_3_5 += i

    return sum_multiple_3_5

# Solution 2:
# numbers divisibles by k lesser than N are numbers in range(0,N,k)
# We can directly sum all the number divisible by 3 by summing all the values in range(0,1000,3) that gives us only multiple of 3.
# Same for number divisible by 5.
# But we count twice the numbers that are divisible by 3 and 5.
# 3 and 5 are prime number, so numbers divisibles by 3 and 5 are numbers divisible by 3*5 = 15.
# We just need to substract the sum of number divisible by 15:

def using_range():
    sum_multiple_3_5 = sum(range(0,1000,3)) + sum(range(0,1000,5)) -sum(range(0,1000,15))
    return sum_multiple_3_5

print(brut_force())
print(using_range())

