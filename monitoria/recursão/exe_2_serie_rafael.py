def serie_2(n, nu = 2, nu_neg = -1, de_neg = 100, pos = False):
    if pos == True:
        res = nu
    else:
        res = nu_neg/de_neg
    if n > 1:
        if pos == True:
            return res + serie_2(n - 1, nu + 2, nu_neg, de_neg, False)
        else:
            return res + serie_2(n - 1, nu, nu_neg - 2, de_neg, True)
    else:
        res = 0
    return res



N = int(input("Dê o número de termos da sequência S2: "))
while N > 0:
    print(f"A soma dos {N} termos da sequência é: {serie_2(N):.4f}")
    N = int(input("Dê o número de termos da sequência S2: "))

"""
S_2 = 0 - 1/100 + 2 - 3/100 + 4 - 5/100 + 6 + ...
"""

# TENTAR USAR EXCEÇÕES NO PROGRAMA PRINCIPAL