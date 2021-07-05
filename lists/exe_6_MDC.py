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

divisores_n_1 = []
for i in range(1, n_1):
    if n_1 % i == 0:
        divisores_n_1.append(i)

divisores_n_2 = []
for i in range(1, n_2):
    if n_2 % i == 0:
        divisores_n_2.append(i)

print(f"Divisores de {n_1}: {divisores_n_1}")
print(f"Divisores de {n_2}: {divisores_n_2}")

lista_mdc = []
# count = 0
for elemento in divisores_n_2:
    if elemento in divisores_n_1:
        lista_mdc.append(elemento)
        # count += 1

# mdc = lista_mdc[count - 1:]
print(f"MDC de {n_1} e {n_2}: {lista_mdc[-1]}")
# print(count)
# print(mdc)