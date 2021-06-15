"""
Calcular o valor de S com N termos, onde N é
informado pelo usuário e S é:
    S = 37*38/1 + 36*37/2 + 35*36/3 + ...
"""
N = int(input("Digite o N (numero de termos): "))
numerador = 38
s = 0
denominador = 1
if N < 0:
    print("O valor de N deve ser maior ou igual a zero.")
else:
    while denominador <= N:
        s += (numerador - 1) * (numerador) / denominador
        print(f"+ {numerador - 1} * {numerador} / {denominador}")
        numerador -= 1
        denominador += 1
    print("-------------")
    print(f"S = {s:_^10.2f}")