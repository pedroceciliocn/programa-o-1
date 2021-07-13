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
while M > 4 or M < 1:
    M = int(input("Dê o número M de linhas da matriz (M <= 4): "))    
N = int(input("Dê o número N de colunas da matriz: "))
while N > 8 or N < 1:
    M = int(input("Dê o número N de colunas da matriz (N <= 8): "))  

matriz = []
for i in range(M):
    matriz.append([0]*N)

vetor = []
for i in range(M): #essa parte ta correta
    for j in range(N):
        matriz[i][j] = int(input(f"Dê o elemento {i+1} {j+1} da matriz: "))
        if matriz[i][j] % 6 == 0: #essa parte ta errada, pq deveria começar pela coluna
            vetor.append(matriz[i][j])

for i in range(M):
    print(matriz[i])

if len(vetor) == 0:
    print("Não há múltiplos de 6 na matriz")
else:
    print(f"Múltiplos de 6 na matriz: {vetor}")