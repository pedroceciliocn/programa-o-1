"""Fazer um programa Python para:
– Ler uma seqüência de números inteiros positivos (ou
zero).
– A leitura deve parar com um número negativo.
– O programa deve imprimir os números lidos cujos
valores têm dois dígitos, mas na ordem inversa em
que forem lidos – o último número lido deve ser o
primeiro a ser impresso."""

lista = []
numero = int(input("Dê um número inteiro positivo (negativo para): "))
# lista.append(numero)
while numero >= 0:
    lista.append(numero)
    numero = int(input("Dê um número inteiro positivo (negativo para): "))
    # lista.append(numero)

maiores = []
for i in range((len(lista) - 1), 0, -1):
    if len(str(lista[i])) == 2:
        maiores.append(lista[i]) # da pra usar .reverse() na lista ao inves do for
print(lista)
print(maiores)