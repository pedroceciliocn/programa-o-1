"""
Ler 2 vetores de tamanho N, com N informado
pelo usuário antes, somar os 2 vetores, imprimir
os 2 vetores e depois o vetor resultado.
"""
N = int(input("Dê o N: "))
while N <= 0:
    N = int(input("Dê o N (maior que 0): "))
v_1 = []
v_2 = []
x = 0
for x in range(N):
    n = int(input(f"Dê o elemento {x} para o vetor 1: "))
    v_1.append(n)

for x in range(N):
    n = int(input(f"Dê o elemento {x} para o vetor 2: "))  
    v_2.append(n)

v_3 = v_1[:]
for i in range(len(v_1)):
    v_3[i] = v_3[i] + v_2[i]
print(f"      v_1 = {v_1}")
print(f"      v_2 = {v_2}")
print(f"v_1 + v_2 = {v_3}")

# v_3 = [v_1[i]+v_2[i] for i in range(len(v_1))] #list comprehension
