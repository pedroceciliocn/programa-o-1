"""
Calcular o fatorial de um número lido.
"""
numero = int(input("De um numero e calcularemos seu fatorial: "))
fatorial = 1
for n in range(1, numero + 1):
    fatorial = fatorial * n

print(fatorial)
