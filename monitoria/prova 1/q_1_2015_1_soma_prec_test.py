"""
Questão 1 - 2015.1 - Faça um programa Python para calcular o valor da série S abaixo. O seu programa deve ler
um valor de precisão (0 < prec <= 0.01 - por exemplo 0.0001) e descobrir qual o número de
termos necessários para que o resultado da série não se modifique dentro da precisão lida. Ou
seja, o primeiro valor N para o qual o valor absoluto (sem sinal) do último termo de S é
menor do que o valor lido, neste exemplo, menor do que 0.0001. No final, além do número de
termos N e do valor da série S (usando 5 casas decimais), o seu programa deve imprimir
também uma lista com todos os resultados parciais calculados da série S (de 1 até N termos).
OBS: Caso precise, pode usar a função abs(a) de Python, que retorna o valor absoluto do
número a.
S = 10 / 1 – 15 / 2 + 20 / 4 – 25 / 8 + 30 / 16 – ...
"""
prec = float(input("Dê a precisão: "))
while 0.01 < prec < 0:
    prec = float(input("Dê a precisão (0 < prec <= 0.01): "))

numerador = 10
denominador = 1
S = numerador/denominador
parciais = [S]
N = 1
# print(f"[1] {numerador}/{denominador}")
while abs(numerador/denominador) > prec:
    numerador += 5
    denominador *= 2
    N += 1
    if N % 2 == 0:
        S -= numerador/denominador
        # print(f"[{N}] {numerador}/{denominador}")
        parciais.append(-numerador/denominador)
    else:
        S += numerador/denominador
        # print(f"[{N}] {numerador}/{denominador}")
        parciais.append(numerador/denominador)

print(f"O menor valor N é: {N}, pois {abs(parciais[-1]):.5f} < {prec}")
print(f'S = {S:.5f}')
print(f"Parciais: {parciais}")

