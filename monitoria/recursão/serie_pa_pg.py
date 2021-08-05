def divisao_2(n , n_0 = 0, p_0 = 1):
    if n <= 1:
        res = n_0/p_0
    else:
        res = n_0 / p_0 + divisao_2(n - 1, n_0 + 2, p_0 * 2)
    return res