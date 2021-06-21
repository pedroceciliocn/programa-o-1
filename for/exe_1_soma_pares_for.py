"""
Somar os inteiros pares entre 50 e 100 (inclusive).
"""
soma = 0
for numero in range(50, 101):
    if numero % 2 == 0:
        soma = soma + numero

print(soma)
