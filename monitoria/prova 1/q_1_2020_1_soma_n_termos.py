"""
Questão 1 - 2020.1 - Faça um programa Python para calcular a soma dos N primeiros termos da série abaixo, 
onde o valor de N deve ser informado pelo usuário no início. O seu programa deve imprimir o 
resultado (com 4 casas decimais) da seguinte forma: “O valor da série com ... termos é ...”. 
 
 S = 19 / 1 – 70 / 5 + 25 / 2 – 85 / 12 + 31 / 4 – 100 / 19 + 37 / 8 ... 
"""

N = int(input("Dê o número N de termos: "))
while N <= 0:
    N = int(input("Dê o número N de termos (maior que 0): "))


numerador_par = 19
numerador_impar = 70
denominador_par = 1
denominador_impar = 5
S = 0

print("S = ", end = "")
for i in range(N):
    if i % 2 == 0:
        S += numerador_par/denominador_par
        print(f"+{numerador_par}/{denominador_par} ", end = "") # para meios de checagem
        numerador_par += 6
        denominador_par *= 2
    else:
        S -= numerador_impar/denominador_impar
        print(f"-{numerador_impar}/{denominador_impar} ", end = "") # para meios de checagem
        numerador_impar += 15
        denominador_impar += 7

print(f"\nO valor da sére com {N} termos é: S = {S:.4f}")

