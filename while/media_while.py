"""
Calcular a média aritmética de vários números
reais fornecidos pelo usuário. A leitura deve
para quando um número negativo for lido.
"""
sair = False
soma = 0
media= 0
i = 0
while not sair:
    n = float(input("Dê o número: "))
    if n < 0:
        sair = True
    else:
        soma += n
        i += 1
print(f"A média é: {soma/i:<.2f}")