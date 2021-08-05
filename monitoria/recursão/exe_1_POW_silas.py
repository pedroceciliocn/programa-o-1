"""
1) Faça uma função recursiva power(base, expoente) que, quando chamada, retorna
base**expoente. Por exemplo: power(3, 4) = 3 * 3 * 3 * 3 = 81. Assuma que o expoente é um
inteiro maior ou igual a 1.
"""

def power(base, expoente):
    if expoente <= 1:
        res = base
    else:
        res = base * power(base, expoente - 1)
    return res

print(power(3, 4))
print(power(3, 3))