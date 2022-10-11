#brute_force
def brut_force(N):
    sum_of_square = 0
    sum_total = 0
    for i in range(N+1):
        sum_total += i
        sum_of_square += i**2
    print(sum_total**2-sum_of_square)

#by formula
# sum of the first N squares is N(N+1)*(2N+1)/6
# sum of the first N integers is N(N+1)/2

def by_formula(N):
    sum_of_square = N*(N+1)*(2*N+1)//6
    square_of_sum = (N*(N+1)//2)**2
    print(square_of_sum - sum_of_square)

brut_force(100)
by_formula(100)

