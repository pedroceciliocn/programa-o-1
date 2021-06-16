"""
Ler um número inteiro N e imprimir o valor do
n-ésimo termo da sequência
    [-1, 0, 5, 6, 11, 12, 17, 18, ...]
"""
N = int(input("De o n e veremos o enésimo termo da sequência [-1, 0, 5, 6, 11, 12, 17, 18, ...]: "))

if N <= 0:
    print("O valor de N deve ser maior que zero.")
else:
    resultado = -1
    l = 1
    for i in range(2, N+1):
        resultado += l
        if i % 2 == 0:
            l = 5
        else:
            l = 1

    print(f"N-ésimo elemento da sequência p/ N = {N} = {resultado}")


