"""
Questão 1 - 2014.2 - Faça um programa Python para calcular a soma dos N primeiros termos da série abaixo. O
valor de N deve ser lido no início e deve ser positivo.

S = 100 / 1! – 13 / 2! + 95 / 3! – 24 / 4! + 90 / 5! – 35 / 6! + ...
"""
quantidade = -1
while quantidade < 0:
  quantidade = int(input("Digite a quantidade de termos: "))

result = 0
valor_par = 100
valor_impar = -13
for x in range(quantidade):
  factorial = 1
  for y in range(x+1, 1, -1):
    if x == 0: pass
    else: factorial *= y

  if x%2 == 0:
    result += valor_par/factorial
    valor_par -= 5
  else:
    result += valor_impar/factorial
    valor_impar -= 11
  
print(result)