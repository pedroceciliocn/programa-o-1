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

numero = int(input("Dê um número inteiro negativo: "))
while numero >= 0:
    numero = int(input("Não é negativo! Dê um primeiro número inteiro negativo: "))

while numero <= 0:
    lista.append(numero)
    numero = int(input("Dê um número inteiro negativo (positivo ou 0 para): "))

for i in range((len(lista) - 1), 0, -1):
    if lista[i] % 5 == 0:
        # print(lista[i])
        cinco.append(lista[i]) #ou usar reverse() sem andar no for de tras pra frente
    if lista[i] % 11 == 0:
        onze.append(lista[i])
        maior = lista[i]

print(f"Múltiplos de 5 digitados: {cinco}")
for i in onze:
    if i > maior:
        maior = i
print(f"Maior múltiplo de 11 digitado: {maior}")
    