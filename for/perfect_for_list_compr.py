# def ifactors(n: int):
#     return [i for i in range(2, n / 2 + 1) if 0 == n % i]
#
#
# print(ifactors(54))




from functools import reduce
from math import sqrt
def factors(n):
        step = 2 if n%2 else 1
        return sorted(reduce(list.__add__,
                    ([i, n//i] for i in range(1, int(sqrt(n))+1, step) if n % i == 0)))


# factors(28)
def perfect(n):
    return [i for i in range(2, n+1) if i == sum(factors(i)) + 1]

print(perfect(28))

# int(sqrt(n))+1