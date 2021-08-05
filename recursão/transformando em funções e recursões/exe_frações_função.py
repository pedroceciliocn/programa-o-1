"""
Calcular o valor de S, onde S é:
    S = 1 + 3/2 + 5/3 + 7/4 + ... + 99/50
"""
# n = -1

# s = 0
# for d in range(1, 51):
#     n += 2
#     s += (n/d)
#     print(f"{n}/{d} +")
# print(f"S = {s:.2f}")


"""agora usando função"""
def S():
    numerador = -1
    soma = 0
    for denominador in range(1, 51):
        numerador += 2
        soma += (numerador/denominador)
        print(f"{numerador}/{denominador} +\n", end = "")
    return soma

print(S())
