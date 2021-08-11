def fatorial(num):
    if num < 2:
        f = 1
    else:
        f = num * fatorial(num - 1)
    return f

# def serie_3(n, nu = 1, de = 5, pos = False):
#     if pos == True:
#         res = fatorial(nu)/de
#     else:
#         res = -fatorial(nu)/de
#     if n > 1:
#         if pos == True:
#             return res + serie_3(n - 1, nu + 1, de + 5, False)
#         else:
#             return res + serie_3(n - 1, nu + 1, de + 5,  True)
#     return res

# def serie_3(n, de = 5, pos = False):
#     if pos == True:
#         res = fatorial(n)/de
#     else:
#         res = fatorial(n)/de * -1
#     if n > 1:
#         if pos == True:
#             return res + serie_3(n - 1, de + 5, False)
#         else:
#             return res + serie_3(n - 1, de + 5, True)
#     return res
# def serie_3(n, nu = 1, de = 5, pos = False) :
#     if n <= 1:
#         if pos == True:
#             res = fatorial(nu) / de 
#         else:
#             res = fatorial(nu)/de * -1
#     else:
#         if pos == False:
#             res = fatorial(nu) / de + serie_3(n - 1, nu + 1, de + 5, True)
#         else:
#             res = fatorial(nu) / de + serie_3(n - 1, nu + 1, de + 5, False)

#     return res

# def serie_3(n, num = 1, den = 5, inc = 5, sin = -1):
# 	if n <= 1:
# 		res = sin * fatorial(n) / den
# 	else:
# 		res = sin * fatorial(n) / den + serie_3(n - 1, num + 1, den + inc, inc + 5, sin * -1)
# 	return res

def serie_3(n, nu = 1, de = 5, pos = True):
    if pos == True:
        res = -fatorial(nu) / de
    else:
        res = fatorial(nu) / de
    if n > 1:
        if pos == True:
            return res + serie_3(n - 1, nu + 1, de + 5, False)
        else:
            return res + serie_3(n - 1, nu + 1, de + 5, True)
    return res


N = int(input("Dê o número de termos da sequência S3: "))
while N > 0:
    print(f"A soma dos {N} termos da sequência é: {serie_3(N):.4f}")
    N = int(input("Dê o número de termos da sequência S3: "))

"""
S_3 = - 1/5 + 2/10 - 6/20 + 24/35 - 120/55 + ...
"""