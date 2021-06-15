"""
Calcular o valor de S com N termos, onde N é
informado pelo usuário e S é:
    S = 2/500 - 5/490 + 2/480 - 5/470 + ...
"""
N = int(input("Digite o N (numero de termos): "))

denominador = 500
S = 0
i = 1
while i <= N:
    if i % 2 == 0:
        S += -5 / denominador
        print(f"-    5/{denominador}")
    else:
        S += 2 / denominador
        print(f"+    2/{denominador}")
    denominador -= 10
    i += 1
print("----------")
print(f"S = {S:.4f}")
