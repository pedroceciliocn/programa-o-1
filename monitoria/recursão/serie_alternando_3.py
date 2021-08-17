"""S3 = 150/20 – 156/30 + 162/50 – 170/80 + 174/120 - 184/170"""

# def serie_S3(n, nu = 150, de = 20, nu_neg = 156, inc = 10, pos = True): 
#     if pos == True:
#         res = nu / de
#     else:
#         res = -nu_neg/de
#     if n > 1:
#         if pos == True:
#             return res + serie_S3(n - 1, nu + 12, de + inc, nu_neg, inc + 10, False)
#         else:
#             return res + serie_S3(n - 1, nu, de + inc, nu_neg + 14, inc + 10, True)
#     return res

# N = int(input("Dê o número de termos da sequência S: "))
# while N > 0:
#     print(f"A soma dos {N} termos da sequência é: {serie_S3(N):.4f}")
#     N = int(input("Dê o número de termos da sequência S: "))
    

# alternativa mudando como usa o sinal
def serie_S3(n, nu = 150, de = 20, nu_neg = -156, inc = 10, pos = True): 
    if pos == True:
        res = nu / de
    else:
        res = nu_neg/de
    if n > 1:
        if pos == True:
            return res + serie_S3(n - 1, nu + 12, de + inc, nu_neg, inc + 10, False)
        else:
            return res + serie_S3(n - 1, nu, de + inc, nu_neg - 14, inc + 10, True)
    return res

N = int(input("Dê o número de termos da sequência S: "))
while N > 0:
    print(f"A soma dos {N} termos da sequência é: {serie_S3(N):.4f}")
    N = int(input("Dê o número de termos da sequência S: "))
    