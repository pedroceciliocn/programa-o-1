"""S2 = 2/500 – 5/490 + 2/480 – 5/470 + ..."""
def serie_S2(N, pos = True, numerador = 2, denominador = 500):
    soma = numerador/denominador
    if N > 1:
        if pos == True:
            return soma + serie_S2(N - 1, False, -5, denominador - 10)
        else:
            return soma + serie_S2(N - 1, True, 2, denominador - 10)
    return soma


N = int(input("Dê o número de termos da sequência S2: "))
while N > 0:
    print(f"A soma dos {N} termos da sequência é: {serie_S2(N):.4f}")
    N = int(input("Dê o número de termos da sequência S1: "))


# #################### alt rafael ###############################################
# def serie_S2(N, pos = True, nu_1 = 2, nu_2 = -5, de = 500):
#     if N <= 1:
#         if pos == True:
#             res = nu_1 / de
#         else:
#             res = nu_2 / de
#     else:
#         if pos == True:
#             res = nu_1 / de + serie_S2(N - 1, False, nu_1, nu_2, de - 10)
#         else:
#             res = nu_2 / de + serie_S2(N - 1, True, nu_1, nu_2, de - 10)
#     return res

# N = int(input("Dê o número de termos da sequência S2: "))
# while N > 0:
#     print(f"A soma dos {N} termos da sequência é: {serie_S2(N):.4f}")
#     N = int(input("Dê o número de termos da sequência S1: "))