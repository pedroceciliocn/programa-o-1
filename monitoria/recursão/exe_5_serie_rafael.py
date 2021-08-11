"""
S_5 = 0 + 1/4 + 0 + 1/16 + 0 + 1/64...
"""

def serie_5(n, nu = 0, de = 2, pos = False):
    if pos == True:
        res = nu / de
    else:
        res = nu / de
    if n > 1:
        if pos == True:
            return res + serie_5(n - 1, 0, de * 2, False)
        else:
            return res + serie_5(n - 1, 1, de * 2, True)
    return res

N = int(input("Dê o número de termos da sequência S5: "))
while N > 0:
    print(f"A soma dos {N} termos da sequência é: {serie_5(N):.4f}")
    N = int(input("Dê o número de termos da sequência S5: "))