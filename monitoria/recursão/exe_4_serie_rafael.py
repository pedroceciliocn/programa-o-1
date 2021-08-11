"""
S_4 = 1/2 + 0 + 1/4 + 0 + 1/8 + 0 + ...
"""

def serie_4(n, nu = 1, de = 2, pos = True):
    if pos == True:
        res = nu / de
    else:
        res = nu / de
    if n > 1:
        if pos == True:
            return res + serie_4(n - 1, 0, de, False)
        else:
            return res + serie_4(n - 1, 1, de * 2, True)
    return res

N = int(input("Dê o número de termos da sequência S4: "))
while N > 0:
    print(f"A soma dos {N} termos da sequência é: {serie_4(N):.4f}")
    N = int(input("Dê o número de termos da sequência S4: "))