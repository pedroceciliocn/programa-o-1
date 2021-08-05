def fibonacci_r(n, t0 = 1, t1 = 0):
    if n <= 1:
        res = t1
    else:
        res = fibonacci_r(n - 1, t1, t0 + t1)
    return res