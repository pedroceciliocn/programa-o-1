"""
Questão 1 2020.3 – Faça um programa Python para calcular a soma dos N primeiros termos da
série abaixo. O valor de N deve ser lido no início e deve ser positivo. Imprimir o resultado
da seguinte forma: “O valor da série com ... termos é ...”.

S = 150 / 20 – 156 / 30 + 162 / 50 – 170 / 80 + 174 / 120 – 184 / 170 + …
"""
N = int(input("Digite o N (numero de termos): "))
n_neg = 156
n_pos = 162

s = 0
print(f"{N} termos da soma: ")
for i in range(0, N):
    if i == 0:
        d = 20
        n = 150
        s += n/d
        print(f"S = {n}/{d} ", end = "")

    elif i % 2 == 0:
        d += 10*i
        s += n_pos/d
        print(f"+ {n_pos}/{d} ", end = "")
        n_pos += 12

    else:
        d += 10*i
        s += -n_neg/d
        print(f"- {n_neg}/{d} ", end = "")
        n_neg += 14

print(f"\nO valor da série com {N} termos é: S = {s:4.2f}")