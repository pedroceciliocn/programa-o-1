"""
Ler um número inteiro e dizer se ele é perfeito ou não.
Obs: um número é perfeito se ele é igual à soma de
todos os seus divisores (exceto ele mesmo).
"""
numero = int(input("De um numero inteiro e direi se ele é perfeito.\n"))

x = 1
soma = 0
while x < numero:
    if numero % x == 0:
        soma += x
    x += 1
if numero == soma:
    print(f"{numero} é perfeito.")
else:
    print(f"{numero} não é perfeito.")

"""
números perfeitos:
{6, 28, 496, 8128, 33550336, 8589869056, …}
"""
