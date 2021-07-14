"""
Q2 – Faça um programa Python para ler uma seqüência de números inteiros negativos – a leitura
pára quando o número zero for lido. No entanto, o usuário só deve poder digitar no máximo
150 números negativos. O programa deve imprimir as seguintes informações como resultado
(nesta ordem):
     Os números lidos cujos valores têm 2 dígitos significativos e também são múltiplos de 5.
A impressão destes números deve ser feita na ordem inversa da que foram lidos.
     O maior número lido que não seja múltiplo de 7.
"""

num = int(input("Dê um número inteiro negativo: "))
while num >= 0:
    num = int(input("Inválido! Dê pelo menos o primeiro negativo e diferente de 0: "))

dois_digitos_multi_cinco = []
maior_nao_multi_sete = 0
continuar = True
while continuar:
    if len(str(abs(num))) == 2 and num % 5 == 0:
        dois_digitos_multi_cinco.append(num)
    if num % 7 != 0 and abs(num) < maior_nao_multi_sete:
        maior_nao_multi_sete = num

    num = int(input("Dê um número inteiro negativo (0 para): "))
    while num > 0:
        num = int(input("Número positivo! Dê um inteiro NEGATIVO! "))
    
    if num !=0 or num <= 150:
        continuar = False

dois_digitos_multi_cinco.reverse()
print(f"Números lidos com 2 dígitos e múltiplos de 5: {dois_digitos_multi_cinco}")
print(f"O maior número lido que não é múltiplo de 7 é: {maior_nao_multi_sete}")
    