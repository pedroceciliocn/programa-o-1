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
valor = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
simbolo = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
numero_romano = ""

N = int(input("Dê um inteiro N: "))
while N <= 0:
    print("Número inválido.")
    N = int(input("Dê um inteiro positivo N: "))
    
for num in range(N):
    x = int(input("Dê um número x inteiro positivo menor que 4000: "))
    while x < 1 or x > 3999:
        x = int(input("Dê um número x inteiro positivo menor que 4000: "))
    i = 0
    num = x
    while num > 0:
        div = num//valor[i]
        num = num % valor[i]
        while div:
            numero_romano += simbolo[i]
            div -= 1
        i += 1
    print(f"{x} -> {numero_romano}")
    numero_romano = ""


