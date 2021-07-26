# Cálculo do fatorial – subprograma recursivo:
def fatorial(num):
    if num < 2:
        f = 1
    else:
        f = num * fatorial(num - 1)
    return f

fat = fatorial(5)
print(fat)