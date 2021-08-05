"""S3 = 2/500 – 5/490 + 2/480 – 5/470 + ..."""
# sem recursao correto #####################################################################################
# def sequencia(N):
#     d = 500
#     s = 0
#     for i in range(1, N + 1):
#         if i % 2 == 0:
#             s += -5/d
#         else:
#             s += 2/d
#         d -= 10
#     return s

# print(sequencia(1))
# print(sequencia(2))
# print(sequencia(3))
# print(sequencia(4))

# # com recursão e correto ################################################################################
"""S3 = 2/500 – 5/490 + 2/480 – 5/470 + ..."""
# def serie_S3(n, pos = True, nu = 2, de = 500):
#     nu_1 = 2
#     nu_2 = -5
#     res = nu / de
#     if n > 1:
#         if pos == True:
#             return res + serie_S3(n - 1, False, nu_2, de - 10)
#         else:
#             return res + serie_S3(n - 1, True, nu_1, de - 10)
#     return res

# # print(serie_S3(1))
# # print(serie_S3(2))
# # print(serie_S3(3))
# # print(serie_S3(4))

# N = int(input("Dê o número de termos da sequência S3: "))
# while N > 0:
#     print(f"A soma dos {N} termos da sequência é: {serie_S3(N):.4f}")
#     N = int(input("Dê o número de termos da sequência S3: "))



# correto e mais enxuto ############################################################################
"""S3 = 2/500 – 5/490 + 2/480 – 5/470 + ..."""
def serie_S3(n, pos = True, nu = 2, de = 500):
    res = nu / de
    if n > 1:
        if pos == True:
            return res + serie_S3(n - 1, False, -5, de - 10)
        else:
            return res + serie_S3(n - 1, True, 2, de - 10)
 
    return res

N = int(input("Dê o número de termos da sequência S3: "))
while N > 0:
    print(f"A soma dos {N} termos da sequência é: {serie_S3(N):.6f}")
    N = int(input("Dê o número de termos da sequência S3: "))


# print(serie_S3(1))
# print(serie_S3(2))
# print(serie_S3(3))
# print(serie_S3(4))

# def series3R (n, num = 2, den = 500)
#     res = num / den
#     if n > 1:
#         if num == 2:
#             res = res + series3(n-1, -5, den - 10)
#         else:
#             res = res + series3(n-1, 2, den - 10)
#     return res

# def series3(n) :
#     return series3R (n, 2, 500)
