# faça um programa que leia x numeros e informe o maior deles
n = int(input("Dê a quantidade de numeros: "))
maior = 0
for x in range(n):
    numero = int(input(f"Dê o {x+1}º numero: "))
    if numero > maior:
        maior = numero
print(f"O maior número foi {maior}")