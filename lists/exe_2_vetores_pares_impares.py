"""Ler uma lista de N números (N é informado pelo
usuário antes), e depois criar duas outras listas
com os números pares e ímpares separados. 
No final imprimir as 3 listas."""
N = int(input("Dê o N: "))
while N <= 0:
    N = int(input("Dê o N (maior que 0): "))

lista = []
for x in range(N):
    numero = int(input(f"Dê o elemento {x} para a lista: "))
    lista.append(numero)

pares = []
impares = []
for elemento in lista:
    if elemento % 2 == 0:
        pares.append(elemento)
    else:
        impares.append(elemento)
print(f"Lista: {lista}")
print(f"Pares: {pares}")
print(f"Ímpares: {impares}")