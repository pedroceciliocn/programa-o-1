"""Fazer subrotinas recursivas para calcular o valor
das seguintes séries – com n termos, onde n deve
ser um parâmetro recebido na chamada:
– S2 = 37*38/1 - 36*37/2 + 35*36/3 – 34*35/4 + ..."""

# def serie_S2(n, nu_1 = 37, nu_2 = 38, de = 1):
#     res = (nu_1) * nu_2 / de
#     if n > 1:
#         return res - serie_S2(n - 1, nu_1 - 1, nu_2 - 1, de + 1)
#     return res

# # print(serie_S2(1))
# # print(serie_S2(2))
# # print(serie_S2(3))
# # print(serie_S2(4))
# # print(serie_S2(5))

# N = int(input("Dê o número de termos da sequência S2: "))
# while N > 0:
#     print(f"A soma dos {N} termos da sequência é: {serie_S2(N):.2f}")
#     N = int(input("Dê o número de termos da sequência S2: "))


# correto e mais enxuto ############################################################
def serie_S2(n, nu = 37, de = 1):
    res = (nu) * ((nu + 1) / de)
    if n > 1:
        return res - serie_S2(n - 1, nu - 1, de + 1)
    return res

# print(serie_S2(1))
# print(serie_S2(2))
# print(serie_S2(3))
# print(serie_S2(4))
# print(serie_S2(5))

N = int(input("Dê o número de termos da sequência S2: "))
while N > 0:
    print(f"A soma dos {N} termos da sequência é: {serie_S2(N):.2f}")
    N = int(input("Dê o número de termos da sequência S2: "))



### outra numa forma diferente (feita na aula)
# def serie_S2(n, nu_1 = 37, nu_2 = 38, de = 1):
#     res = (nu_1) * nu_2 / de
#     if n > 1:
#         if de % 2 == 1:
#             res = res - serie_S2(n - 1, nu_1 - 1, nu_2 - 1, de + 1)
#         else:
#             res = res + serie_S2(n - 1, nu_1 - 1, nu_2 - 1, de + 1)
#     return res


### outra forma diferente
# def series2(n, numl = 37, den = 1, sinal = 1):
#     res = sinal * num1 * (num1 + 1) / den
#     if n > 1 :
#         res = res + series2(n - 1, num1 - 1, den + 1, - sinal)
#     return res