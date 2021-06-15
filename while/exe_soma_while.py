"""
Somar os inteiros pares entre 50 e 100 (inclusive).
"""
soma = 0
n = 49
while n <= 100:
    if n % 2 == 0:
        soma += n
    n += 1
print(soma)
