"""
Calcular o valor de S com N termos, onde N é
informado pelo usuário e S é:
    S = 2/500 - 5/490 + 2/480 - 5/470 + ...
"""

# N = int(input("Digite o N (numero de termos): "))

# d = 500
# s = 0
# for i in range(1, N+1):
#     if i % 2 == 0:
#         s += -5/d
#         print(f"- 5/{d}")
#     else:
#         s += 2/d
#         print(f"+ 2/{d}")
#     d -= 10    
# print("____________")
# print(f"S = {s:.4f}")


"""usando função"""

# def serie_n_termos(N):
#     soma = 0
#     denominador = 500
#     for i in range(1, N+1):
#         if i % 2 == 0:
#             soma += -5/denominador
#         else:
#             soma += 2/denominador
#         denominador -= 10
#     return soma

# print(serie_n_termos(1))

"""usando recursão"""

def serie_n_termos_recursivo(N, pos = True, numerador = 2, denominador = 500):
    soma = numerador/denominador
    if N > 1:
        if pos == True:
            return soma + serie_n_termos_recursivo(N - 1, False, -5, denominador - 10)
        else:
            return soma + serie_n_termos_recursivo(N - 1, True, 2, denominador - 10)
    return soma

print(serie_n_termos_recursivo(2))
