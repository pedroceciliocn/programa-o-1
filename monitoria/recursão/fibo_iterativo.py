def fibonacci_i(n):
    t0 = 1
    t1 = 0
    if n == 1:
        res = t1
    else:
        for i in range(n - 1):
            res = t0 + t1
            t0, t1 = t1, res
    return res