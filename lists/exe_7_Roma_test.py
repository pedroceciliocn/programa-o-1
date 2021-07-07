valor = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
simbolo = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
numero_romano = ""
listaNumeros = []
j = 0
n = int(input("Dê um número N inteiro positivo menor que 4000: "))
while n > 0:
    listaNumeros.append(n)
    n = int(input("Dê um número N inteiro positivo menor que 4000: "))
listaNumerosTransformados = [0] * len(listaNumeros)
#rodando
for num in listaNumeros:
    i = 0
    while num > 0:
        div = num//valor[i]
        num = num % valor[i]
        while div:
            numero_romano += simbolo[i]
            div -= 1
        i += 1
    listaNumerosTransformados[j] = numero_romano
    j += 1

for m in range(len(listaNumeros)):
    print(f"{listaNumeros[m]} -> {listaNumerosTransformados[m]}")


