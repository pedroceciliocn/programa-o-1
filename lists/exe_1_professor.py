"""
Ler 2 vetores de tamanho N, com N informado
pelo usuário antes, somar os 2 vetores, imprimir
os 2 vetores e depois o vetor resultado.
"""
N = int(input("Dê o N: "))
while N <= 0:
    N = int(input("Dê o N (maior que 0): "))

v_1 = [0]*N
v_2 = [0]*N
res = [0]*N

for i in range(N):
    n = int(input(f"Dê o elemento {i} para o vetor 1: "))
    v_1[i] = n

for i in range(N):
    n = int(input(f"Dê o elemento {i} para o vetor 2: "))  
    v_2[i] = n
    res[i] = v_1[i] + v_2[i]

print(f"      v_1 = {v_1}")
print(f"      v_2 = {v_2}")
print(f"v_1 + v_2 = {res}")
