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
prec = float(input("Dê o valor de precisão (0 < prec <= 0.01): "))
while prec <= 0 or prec > 0.01:
    prec = float(input("Dê o valor de precisão (0 < prec <= 0.01): "))

N = int(input("Dê o N: "))
while N <= 0:
    N = int(input("N inválido. Dê um N maior que 0: "))

# NÃO É PRA PEDIR O N, É PRA DESCOBRIR!!
S = 0
numerador_impar = 10
numerador_par = -15
denominador = 1

parciais = []
for i in range(1, N+1):
    if i % 2 == 0:
        S -= numerador_par/denominador
        print(f"[{i}] {numerador_par}/{denominador}") # para meios de checagem
        parciais.append(numerador_par/denominador)
        numerador_par -= 10
    else:
        S += numerador_impar/denominador
        print(f"[{i}] +{numerador_impar}/{denominador}") # para meios de checagem
        parciais.append(numerador_impar/denominador)
        numerador_impar += 10
    denominador *= 2
print(f"Resultado: S = {S:.5f}")
print(f"Parciais: {parciais}")

for i in range(N-1, 0, -1):
    if abs(parciais[i]) < prec:
        parcial_N = abs(parciais[i])
        menor_N = i
print(f"O menor valor N é: {menor_N + 1}, pois {parcial_N:.5f} < {prec}")

