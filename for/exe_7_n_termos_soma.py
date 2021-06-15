N = int(input("Digite o N (numero de termos): "))
numerador = 38
s = 0

if N < 0:
    print("O valor de N deve ser maior ou igual a zero.")
else:
    for denominador in range(1, N+1):
        s += (numerador - 1) * (numerador) / denominador
        print(f"+ {numerador - 1} * {numerador} / {denominador}")
        numerador -= 1
    print("_____________")
    print(f"S =   {s:.2f}")


