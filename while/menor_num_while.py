"""
Calcular o menor de uma série de números inteiros
lidos. A leitura dos números deve parar quando o
número zero for lido.
"""
sair = False
n = int(input("Dê o inteiro: "))
menor = n
while not sair:
    n = int(input("Dê o inteiro:"))
    if n == 0:
        sair = True
    else:
        if n < menor:
            menor = n
print(f"O menor numero é {menor}.")



