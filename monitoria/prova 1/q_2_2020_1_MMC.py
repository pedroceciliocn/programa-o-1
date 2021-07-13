"""
Questão 2 - 2020.1 – O Mínimo Múltiplo Comum (MMC) de 2 números inteiros positivos é definido como o 
menor número inteiro positivo que é múltiplo de ambos. Faça um programa Python para ler 2 
números inteiros positivos no início e procurar/descobrir o MMC destes 2 números.
"""

n_1 = int(input("Dê o primeiro número: "))
while n_1 <= 0:
    n_1 = int(input("Dê o primeiro número (inteiro positivo): "))
n_2 = int(input("Dê o segundo número: "))
while n_2 <= 0:
    n_2 = int(input("Dê o segundo número (inteiro positivo): "))

if n_1 > n_2:
    MMC = n_1
    while MMC % n_2 != 0:
        MMC += n_1
else:
    MMC = n_2
    while MMC % n_1 != 0:
        MMC += n_2

print(f"O MMC entre {n_1} e {n_2} é: {MMC}")