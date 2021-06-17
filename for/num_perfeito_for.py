"""
Ler um número inteiro e dizer se ele é perfeito ou não.
Obs: um número é perfeito se ele é igual à soma de
todos os seus divisores (exceto ele mesmo).
"""
from pytictoc import TicToc
numero = int(input("De um numero inteiro e direi se ele é perfeito.\n"))
t = TicToc()
x = 1
soma = 0
t.tic()
for x in range(1, numero):
    if numero % x == 0:
        soma += x
if numero == soma:
    print(f"{numero} é perfeito.")
else:
    print(f"{numero} não é perfeito.")
t.toc()
print(t)
"""
números perfeitos:
{6, 28, 496, 8128, 33550336, 8589869056, …}
"""