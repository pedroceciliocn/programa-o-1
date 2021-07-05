"""
Fazer um programa Python para:
– Ler por linhas uma matriz M x N, onde M <= 4 e N <= 8
são lidos antes da leitura da matriz.
– Depois, percorrendo a matriz por colunas, armazenar
em um vetor os elementos desta matriz que sejam
múltiplos de 6.
– Finalmente, imprimir de maneira organizada a matriz e
depois o vetor.
"""
M = int(input("Dê o número M de linhas da matriz: "))
while M > 4:
    M = int(input("Dê o número M de linhas da matriz (M <= 4): "))    
N = int(input("Dê o número N de colunas da matriz: "))
while N > 8:
    M = int(input("Dê o número N de colunas da matriz (N <= 8): "))  

m = []
for i in range(M):
    m.append([0]*N)

v = []
for i in range(M):
    for j in range(N):
        m[i][j] = int(input(f"Dê o elemento i = {i+1} j = {j+1} da matriz: "))
        if m[i][j] % 6 == 0:
            v.append(m[i][j])

for i in range(M):
    print(m[i])

if len(v) == 0:
    print("Não há múltiplos de 6 na matriz")
else:
    print(f"Múltiplos de 6 na matriz: {v}")