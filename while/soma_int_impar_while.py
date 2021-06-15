"""
Somar os inteiros ímpares entre dois valores
inteiros informados pelo usuário.
"""
n_1 = int(input("De o primeiro valor do intervalo: "))
n_2 = int(input("De o segundo valor do intervalo: "))
s = 0
if n_1 > n_2:
    n_1, n_2 = n_2, n_1
i = n_1
while i < n_2:
    if i % 2 != 0:
        s += i
    i += 1
print(s)

