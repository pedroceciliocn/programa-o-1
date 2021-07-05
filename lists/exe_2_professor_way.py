"""Ler uma lista de N números (N é informado pelo
usuário antes), e depois criar duas outras listas
com os números pares e ímpares separados. 
No final imprimir as 3 listas."""
N = int(input("Dê o N: "))
while N <= 0:
    N = int(input("Dê o N (maior que 0): "))

lista = [0]*N
pares = [0]*N
impares = [0]*N
len_impar = 0
len_par = 0
for i in range(N):
    numero = int(input(f"Dê o elemento {i} para a lista: "))
    lista[i] = numero
    if numero % 2 != 0:
        impares[len_impar] = numero
        len_impar += 1
    else:
        pares[len_par] = numero
        len_par += 1

impares = impares[:len_impar]
pares = pares[:len_par]
print(f"Lista: {lista}")
print(f"Pares: {pares}")
print(f"Ímpares: {impares}")