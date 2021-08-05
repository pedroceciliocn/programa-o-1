"""
Somar os inteiros pares entre 50 e 100 (inclusive). Só que agora definindo uma função.
"""
soma = 0
for numero in range(50, 101, 2): # outra forma de somar somente os pares
    soma = soma + numero

print(soma)

"""Função definida"""
def soma_pares_intervalo(inicio, fim):
    soma = 0
    for numero in range(inicio, fim + 1, 2):
        soma += numero
    return soma


