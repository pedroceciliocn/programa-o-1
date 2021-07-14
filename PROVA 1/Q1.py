"""
Q1 – Faça um programa Python para calcular a soma dos N primeiros termos da série abaixo,
onde o valor de N deve ser informado pelo usuário no início. O seu programa deve imprimir o
resultado (com 4 casas decimais) da seguinte forma: “O valor da série com ... termos é ...”.
S = 2 – 7 / 5 + 8 / 3 – 13 / 9 + 32 / 9 – 19 / 13 + 128 / 27 ...
"""

N = int(input("Dê o N: "))
while N <= 0:
    N = int(input("N inválido! Dê o N inteiro e positivo: "))

S = 0
numerador_neg = 7
numerador_pos = 2 
denominador_pos = 1
denominador_neg = 5 

print(f"S = ", end = "")
for i in range(1, N+1):
    if i % 2 == 0:
        S -= numerador_neg/denominador_neg
        print(f" -{numerador_neg}/{denominador_neg}", end = "") # para checagem
        numerador_neg += 6
        denominador_neg += 4
    else:
        S += numerador_pos/denominador_pos
        print(f" +{numerador_pos}/{denominador_pos}", end = "") # para checagem
        numerador_pos *= 4
        denominador_pos *= 3
print(f"\nO valor da série com {N} termos é: ")
print(f"S = {S:.4f}")
