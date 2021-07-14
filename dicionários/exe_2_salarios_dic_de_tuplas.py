"""
Exercício slide (último de tabelas antes da prova)
Fazer um programa para:
– Ler uma tabela de pessoas onde:
    • Cada pessoa tem código (int), nome (Str) e salário (float).
    • A leitura da tabela pára com um código <= 0.
– Depois o usuário informará um valor máximo de salário.
Caso o valor não seja positivo, o programa deve
apontar o erro e pedir os dados novamente.
– O programa deve imprimir os dados das pessoas cujos
salários sejam menores que o valor máximo informado,
seguidos pelo número de pessoas correspondentes, e
pela média dos salários destas pessoas.
"""

codigo = int(input("Dê o código da pessoa: "))
while codigo <= 0:
    codigo = int(input("Inválido. Dê um código inteiro e positivo: "))

tabela = {}
n = 0
while codigo > 0:
    nome = input("Dê o nome da pessoa: ")
    salario = float(input("Dê o salário da pessoa: "))
    while salario <= 0:
        salario = float(input("Salário inválido! Dê o salário da pessoa (positivo!): "))
    tabela[codigo] = (nome, salario) #dicionario de tuplas
    n += 1

    codigo = int(input("Dê o código da pessoa (0 ou negativo para parar): ")) 
    while codigo in tabela:   
        codigo = int(input("Código repetido! Dê um código novo para a pessoa (0 ou negativo para parar): ")) 

print(f"Tabela com {n} pessoas lida corretamente.")

maximo = float(input("Dê um valor de salário máximo: "))
while maximo <= 0:
    maximo = float(input("Dê um valor de salário máximo POSITIVO: "))

qtd = 0
soma = 0
print(f"Pessoas na faixa inferior a R$ {maximo:.2f} de salário: ")
for codigo in tabela:
    if tabela[codigo][1] < maximo:
        print(f"\tCódigo: {codigo}; Nome: {tabela[codigo][0]}; Salário: {tabela[codigo][1]:.2f}")
        qtd += 1
        soma += tabela[codigo][1]

if qtd == 0:
    print(f"Nenhuma pessoa encontrada na faixa inferior a R$ {maximo:.2f} de salário")
else:
    print(f"Total de pessoas nessa faixa: {qtd} ")
    print(f"Média de salários nessa faixa: R$ {soma/qtd:.2f}")
    
