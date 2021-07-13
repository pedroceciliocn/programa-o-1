"""
Questão 2 – Faça um programa Python para ler uma seqüência de números inteiros
negativos – a leitura para quando um número não negativo for lido. No entanto, o usuário
só deve poder digitar no máximo 300 números negativos. O programa deve imprimir as
seguintes informações como resultado (nesta ordem):
    • Os números lidos cujos valores são negativos e são múltiplos de 5. A impressão
    destes números deve ser feita na ordem inversa da que foram lidos.
    • O maior número lido que seja múltiplo de 11.
"""
lista = []
cinco = []
onze = []
maior = 0
contador = 0

numero = int(input("Dê um número inteiro negativo: "))
while numero >= 0:
    numero = int(input("Não é negativo! Dê um primeiro número inteiro negativo: "))
while numero < 0 and contador < 300:
    lista.append(numero)
    contador += 1
    if abs(numero) % 5 == 0: #usando modulo (valor absoluto)
        cinco.append(numero) 
    if abs(numero) % 11 == 0 and abs(numero) > maior: #usando modulo (valor absoluto)
        maior = numero
    numero = int(input("Dê um número inteiro negativo (positivo para sair): "))
cinco.reverse()
print(f"Múltiplos de 5 digitados: {cinco}")
print(f"Maior múltiplo de 11 digitado: {maior}")