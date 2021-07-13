"""
Questão 2 - 2015.1 - Faça um programa Python para ler uma seqüência de números inteiros – a leitura pára
quando o número zero for lido. O programa deve imprimir as seguintes informações como
resultado (nesta ordem):
     A quantidade total de números digitados.
     O maior número lido que seja múltiplo de 11.
     Os números lidos cujos valores têm 3 dígitos significativos. A impressão destes números
    deve mostrar primeiro os números negativos (de 3 dígitos) e depois os positivos (idem).
     A média aritmética dos números impressos no item anterior (todos os de 3 dígitos).
"""

tres_digitos = []
maior = 0
n = 0
num = int(input("Dê um inteiro (0 para): "))
while num != 0:
    n += 1
    if len(str(abs(num))) == 3:
        tres_digitos.append(num)
    if num % 11 == 0:
        if abs(num) > maior:
            maior = num
    num = int(input("Dê um inteiro (0 para): "))
print(f"{n} números lidos")

soma = 0
contador = 0
if len(tres_digitos) > 0:
    tres_digitos.sort()
    print(f"Números com 3 dígitos: {tres_digitos}")
    for i in tres_digitos:
        soma += i
        contador += 1
    print(f"Média dos {contador} números com 3 dígitos: {soma/contador:.2f}")
else:
    print("Não haviam números com 3 dígitos")

if maior != 0:
    print(f"O maior múltiplo de 11 digitado foi: {maior}")
else:
    print("Não haviam múltiplos de 11")