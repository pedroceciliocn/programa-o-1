i = num = soma = 0
qtd = int(input("Digite a quantidade de numeros: "))
for i in range(qtd):
    num = int(input("Digite um numero: "))
    soma += num
print(f"A soma dos {qtd} numeros digitados é {soma}")
