"""Fazer um programa Python para:
– Ler uma seqüência de números inteiros positivos (ou
zero).
– A leitura deve parar com um número negativo.
– O programa deve imprimir os números lidos cujos
valores têm dois dígitos, mas na ordem inversa em
que forem lidos – o último número lido deve ser o
primeiro a ser impresso."""

lista = []
while True:
    numero = int(input("Dê um número inteiro positivo (negativo para): "))
    if numero < 0:
        break
    else:
        lista.append(numero)

# duplo = []
# print(lista[-1])
for i in range((len(lista) - 1), 0, -1):
    if len(str(lista[i])) == 2:
        # duplo.append(lista[i])
        print(lista[i])

# print(lista[-1])
# for elemento in duplo:
#     print(elemento)
# print(lista)


