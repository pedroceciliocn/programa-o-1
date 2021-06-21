"""
Somar os inteiros pares entre 50 e 100 (inclusive).
"""
soma = 0
for numero in range(50, 101, 2): # outra forma de somar somente os pares
    soma = soma + numero

print(soma)
