dois_cinco = []
contador = 0

numero = int(input("Dê um número inteiro negativo: "))
while numero >= 0:
    numero = int(input("Não é negativo! Dê um primeiro número inteiro negativo: "))
maior = numero
while numero < 0 and contador < 150:
    contador += 1
    if len(str(abs(numero))) == 2 and abs(numero) % 5 == 0: #usando modulo (valor absoluto)
        dois_cinco.append(numero) 
    if numero % 7 != 0 and (numero) > maior: #usando modulo (valor absoluto)
        maior = numero
    numero = int(input("Dê mais um número inteiro negativo (0 sair): "))
dois_cinco.reverse()

if len(dois_cinco) == 0:
    print("Nenhum número com dois dígitos e também múltiplo de 5 digitado!")
else:
    print(f"Números com dois dígitos e múltiplos de 5 digitados: {dois_cinco}")
print(f"Maior não múltiplo de 7 digitado: {maior}")