"""
Questão 1 - 2014.2 - Faça um programa Python para calcular a soma dos N primeiros termos da série abaixo. O
valor de N deve ser lido no início e deve ser positivo.

S = 100 / 1! – 13 / 2! + 95 / 3! – 24 / 4! + 90 / 5! – 35 / 6! + ...
"""
N = int(input("Dê o N: "))
while N <= 0:
    N = int(input("N inválido. Dê um N maior que 0: "))

S = 0
numerador_impar = 100
numerador_par = 13
denominador = 1
fatorial = 1

print("S = ", end = "")
for i in range(1, N+1):
    if i % 2 == 0:
        S -= numerador_par/fatorial
        print(f"- {numerador_par}/{denominador}! ", end = "") # para fins de checagem
        numerador_par += 11
    else:
        S += numerador_impar/fatorial
        print(f"+ {numerador_impar}/{denominador}! ", end = "") # para fins de checagem
        numerador_impar -= 5
    denominador += 1
    fatorial = fatorial * denominador

print(f"\nResultado: S = {S:.2f}")