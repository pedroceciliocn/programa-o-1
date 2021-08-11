"""
S1 = 37*38/1 - 36*37/2 + 35*36/3 - 34*35/4...
"""
def serie_S3(n, nu = 150, de = 20, nu_neg = -156, de_neg = 30, pos = True):
    if pos == True:
        res = nu / de
    else:
        res = nu_neg/de_neg
    if n > 1:
        if pos == True:
            return res + serie_S3(n - 1, nu + 12, de * 2.5, nu_neg, de_neg, False)
        else:
            return res + serie_S3(n - 1, nu, de, nu_neg - 14, de_neg * 2.5, True)
    return res

# def esconder_serie_S1(n):
#     return serie_S1(n)


N = int(input("Dê o número de termos da sequência S1: "))
while N > 0:
    print(f"A soma dos {N} termos da sequência é: {serie_S3(N):.2f}")
    N = int(input("Dê o número de termos da sequência S1: "))


