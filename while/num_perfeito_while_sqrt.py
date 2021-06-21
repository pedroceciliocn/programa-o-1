"""
Ler um número inteiro e dizer se ele é perfeito ou não.
Obs: um número é perfeito se ele é igual à soma de
todos os seus divisores (exceto ele mesmo).
"""
# import math
numero = int(input("Dê um número inteiro e direi se ele é perfeito: "))
while numero <= 0:
    numero = int(input("Dê um número maior que 0: "))
# x = 1
# soma = 0
# raiz = int(math.sqrt(numero)) corrigir depois
#
# while x <= raiz:
#     if numero % x == 0:
#         soma += 1
#     else:
#         soma +=1
#         soma += numero//1
# if numero == soma:
#     print(f"{numero} é perfeito.")
# else:
#     print(f"{numero} não é perfeito.")

"""
números perfeitos:
{6, 28, 496, 8128, 33550336, 8589869056, …}
"""