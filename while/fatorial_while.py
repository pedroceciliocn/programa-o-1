"""
Calcular o fatorial de um número lido.
"""
n = int(input("De um numero e calcularemos o fatorial dele: "))
fatorial = 1
x = 1
while x <= n:
    fatorial = fatorial * x
    x += 1
print(fatorial)
