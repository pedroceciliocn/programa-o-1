"""
Construir uma tabela de conversão de graus
Fahreinheit para Celsius, para todos os
Fahrenheit em um intervalo informado pelo
usuário. Obs: C = (F - 32) * 5 / 9
"""
f_1 = int(input("De o primeiro numero do intervalo em °F: "))
f_2 = int(input("De o segundo numero do intervalo em °F: "))
if f_1 > f_2:
    f_1, f_2 = f_2, f_1
# f = f_1
while f_1 <= f_2:
    c = (f_1 - 32) * (5 / 9)
    print(f"{f_1:2}°F = {c:.2f}ºC")
    f_1 += 1
