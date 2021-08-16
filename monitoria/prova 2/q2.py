def fatorial(n):
    if n <= 1:
        fat = 1
    else:
        fat = n * fatorial(n - 1)
    return fat

def Soma(N, num_1 = 3, num_2 = 5/6, den = 1, sin = 1):
    if N <= 1:
        if sin > 0 :
            res = num_1 / fatorial(den)
        else:
            res = num_2 / fatorial(den)
    else:
        if sin > 0:
            res = num_1 / fatorial(den) + Soma(N - 1, num_1, num_2 * 6, den + 1, sin * -1)
        else:
            res = num_2 / fatorial(den) + Soma(N - 1, num_1 * 5, num_2, den + 1, sin * -1) 
    return res          


erro = True
while erro:
    try:
        N = int(input("Digite um número inteiro: "))
        erro = False
    except:
        print("Erro.")

res = Soma(N)
print(res)
    

# print(Soma(1))
# print(Soma(2))
# print(Soma(3))
# print(Soma(4))
# print(Soma(5))
# print(Soma(6))