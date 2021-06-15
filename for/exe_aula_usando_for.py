# le n numeros e mostra o menor deles

qtd = int(input("De a quantidade de numeros: "))
menor = numero = 0

if qtd <= 0:
    print("A quantidade deve ser maior que zero.")
else:
    numero = int(input("Digite o numero: "))
    menor = numero
    for i in range(qtd-1): # ou range(1, qtd):
        numero = int(input("Digite o numero: "))
        if (numero < menor):
            menor = numero

    print(f"O menor numero digitado foi {menor}")
