"""
O máximo divisor comum (MDC) de 2 números inteiros é o maior número inteiro que divide ambos
sem deixar resto. Faça um programa Python para:
    - Ler 2 números inteiros - verificar se são positivos
    - Determinar o MDC destes 2 números
    - OBS: não use fórmulas matemáticas
"""
n_1 = int(input("Dê o primeiro inteiro: "))
while n_1 <= 0:
    n_1 = int(input("Dê o primeiro inteiro (positivo): "))
if n_1 > 0:
    print(f"{n_1} é positivo.")
n_2 = int(input("Dê o segundo inteiro: "))
if n_2 > 0:
    print(f"{n_2} é positivo.")
while n_2 <= 0:
    n_2 = int(input("Dê o segundo inteiro (positivo): "))

if n_1 >= n_2:
    N = n_1
else:
    N = n_2

MDC = 0
for i in range(1, N):
    if n_1 % i == 0 and n_2 % i == 0:
        MDC = i
print(f"MDC de {n_1} e {n_2}: {MDC}")
