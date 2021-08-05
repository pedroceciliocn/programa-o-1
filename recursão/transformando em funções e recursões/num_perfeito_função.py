# Ler um número inteiro e dizer se ele é perfeito ou não.
# n = int(input('digite aqui um valor: '))
# sequenciaPerfeitos = 0
# i = 1
# ehPerfeito = False
# while n <= 0:
#     n = int(input("Dê um número maior que 0: "))
# else:
#     for (i, sequenciaPerfeitos): #isso é uma recursao, daria pra melhorar e tá errado
#         sequenciaPerfeitos = (2 ** (i -1)) * ((2 ** i) - 1)
#         if sequenciaPerfeitos == n:
#             ehPerfeito = True
#         print(sequenciaPerfeitos)

# print(ehPerfeito)


# correto
# numero = int(input("De um numero inteiro e direi se ele é perfeito.\n"))
# x = 1
# soma = 0
# for x in range(1, numero):
#     if numero % x == 0:
#         soma += x
# if numero == soma:
#     print(f"{numero} é perfeito.")
# else:
#     print(f"{numero} não é perfeito.")


# usando função
def é_perfeito(numero):
    x = 1
    soma = 0
    for x in range(1, numero):
        if numero % x == 0:
            soma += x
    if numero == soma:
        return True
    else:
        return False

"""
números perfeitos:
{6, 28, 496, 8128, 33550336, 8589869056, …}
"""
print(é_perfeito(6))