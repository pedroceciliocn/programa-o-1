"""
Faça uma subrotina Python do tipo função recursiva para calcular a soma dos N primeiros
termos da série abaixo, onde o valor de N é um parâmetro e o resultado do cálculo da série é o
resultado da função. Observe que o símbolo “!” se refere ao fatorial do número e também que
você não pode usar os comandos de repetição nesta questão.
S = 3 + 5 / 2! + 15 / 3! + 30 / 4! + 75 / 5! + 180 / 6! + ...

OBS - Você pode (ou não) incluir um programa principal para ler um valor de N e testar a sua
função: somente a função será avaliada na correção.
"""

def fatorial(num):
    if num < 2:
        f = 1
    else:
        f = num * fatorial(num - 1)
    return f

# def serie(n, nu = 5, nu_neg = 15, de = 2, pos = True):
#     if pos == True:
#         res = nu / fatorial(de)
#     else:
#         res = nu_neg / fatorial(de)
#     if n > 1:
#         if pos == True:
#             # print(f"{nu}/{de}")
#             return res + serie(n - 1, nu * 6, nu_neg, de + 1, False)
#         else:
#             # print(f"{nu_neg}/{de}")
#             return res + serie(n - 1, nu, nu_neg * 5, de + 1, True)
#     else:
#         res = 3
#     return res

def serie(n, nu = 3, nu_neg = 5, de = 1, pos = True):
    if pos == True:
        res = nu / fatorial(de)
    else:
        res = nu_neg / fatorial(de)
    if n > 1:
        if pos == True:
            return res + serie(n - 1, nu * 5, nu_neg, de + 1, False)
        else:
            return res + serie(n - 1, nu, nu_neg * 6, de + 1, True)
    return res


# DEPOIS FAZER A FUNÇÃO PRINCIPAL COM TRATAMENTO DE EXCEÇÕES
print(serie(1))
print(serie(2))
print(serie(3))
print(serie(4))
print(serie(5))
print(serie(6))