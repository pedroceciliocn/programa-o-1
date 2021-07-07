"""
Desenvolva um algoritmo
que tenha como entrada
números que serão
adicionados a uma lista (o
usuário deverá decidir
quantos números
adicionar). Criada a lista, o
algoritmo deverá ordenar
os números desse array.

obs: Não pode usar o
método sort
"""
N = int(input("Dê o número N de elementos da lista: "))
while N <= 0:
    N = int(input("Dê o número N de elementos da lista (maior que 0): "))

L = []
for i in range(N):
    num = int(input(f"Dê o elemento {i} da lista: "))
    L.append(num)
print(f"Lista: {L}")
fim = N # qtd de elementos da lista. no bubble sort nao precisamos verificar o ultimo elemento apos uma passagem completa
while fim > 1: #
    trocou = False
    x = 0
    while x < (fim - 1):
        if L[x] > L[x + 1]:
            trocou = True
            temp = L[x]
            L[x] = L[x + 1]
            L[x + 1] = temp
        x += 1
    if not trocou:
        break
    fim -= 1

print(f"Lista ordenada: {L}")