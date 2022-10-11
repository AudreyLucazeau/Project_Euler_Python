# To avoid recursive function we keep the value in a list

def sum_even_fibonacci(N):
    fibonacci_serie = [1,2]
    sum_even_number = 2
    while fibonacci_serie[-1]<N:
        fibonacci_serie.append(fibonacci_serie[-1]+fibonacci_serie[-2])
        if fibonacci_serie[-1]%2 == 0:
            sum_even_number += fibonacci_serie[-1]

    #if the last number (so greater than N) is even, we have to decrease it from the total sum.
    if fibonacci_serie[-1]%2 == 0:
        sum_even_number -= fibonacci_serie[-1]

    print(fibonacci_serie)
    return sum_even_number

print(sum_even_fibonacci(4000000))
