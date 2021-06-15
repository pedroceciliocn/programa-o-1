numeros_vetor = []
flag = True

while flag == True:
    numero = input("De um numero ou tecle 'n' para parar: ")
    if numero == 'n':
        flag = False
    else:
        numero = float(numero)
        numeros_vetor.append(numero)
print(f"Os numeros são {numeros_vetor[0], numeros_vetor[1], numeros_vetor[2]} e a média aritmética deles é {sum(numeros_vetor)/3}.")
