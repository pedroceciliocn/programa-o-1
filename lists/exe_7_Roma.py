"""
Fazer um programa Python para:
– Ler um número inteiro positivo N digitado pelo usuário -
o programa deve verificar se o valor de N é válido.
– Depois, ler N números inteiros positivos (0 < x < 4000)
e, para cada um deles, imprimir a sua representação
em algarismos romanos.
– Construir o resultado (valor em algarismos romanos)
usando um String.
– OBS. Lembre que os valores dos algarismos romanos
são: I=1, V=5, X=10, L=50, C=100, D=500, e M=1000,
e que IV=4, IX=9, XL=40, XC=90, CD=400 e CM=900.
"""
N = int(input("Dê um inteiro N: "))
while N <= 0:
    print("Número inválido.")
    N = int(input("Dê um inteiro positivo N: "))

valor = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
simbolo = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
numero_romano = ""
i = 0
for x in range(N):
    n = int(input("Dê um numero: "))
    num = n
    while num > 0:
        div = num//valor[i]
        num = num % valor[i]
        while div:
            numero_romano += simbolo[i]
            div -= 1
        i += 1
    print(numero_romano)







