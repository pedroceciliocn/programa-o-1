"""
Faça um programa Python para ler uma tabela de pessoas onde:
     Cada pessoa tem um cpf (long), um nome (String) e um salário (float).
     A leitura da tabela pára com um cpf que não seja positivo.
Depois o usuário informará um intervalo de salários, ou seja, os limites inferior e superior do
intervalo. Ambos devem ser positivos, mas o limite inferior pode ser zero. Além disto, o
limite inferior do intervalo deve ser menor do que o limite superior. Caso alguma destas
restrições seja violada, o programa deve informar o erro ao usuário e pedir os dados
novamentre. De posse de um intervalo correto, o programa deve imprimir os dados das
pessoas que se enquadram no intervalo, seguidos pelo número de pessoas do intervalo, e pela
média dos salários destas pessoas.
"""
# leitura
tab = {}
n = 0
soma = 0

cpf = int(input("CPF (negativo para parar): "))
while cpf < 0:
    cpf = int(input("Inválido. Digite novamente a CPF (negativo para parar): "))

while cpf != 0: #incossistencia
    nome = input("Nome da pessoa: ")
    salario = float(input("Salário da pessoa: "))
    while salario < 0:
        salario = float(input("Inválido. Digite novamente o salario da pessoa: "))
    tab[cpf] = (nome, salario)
    n += 1

    cpf = int(input("CPF (0 ou negativo para parar): "))
    while cpf in tab or cpf < 1:
        print("fim")
        break
        # cpf = int(input("Repetido. Digite novamente a CPF da pessoa (0 ou negativo para parar): "))

print(f"Tabela com {n} pessoas lida corretamente.\n {tab}")

#consulta
N = int(input("Dê o N de intervalos a pesquisar: "))
while N < 1:
    N = int(input("Inválido. Dê o N de intervalos a pesquisar: "))

for i in range(N):
    min = float(input(f"Dê o {i+1}º intervalo mínimo de salário: "))
    if min < 0:
        min = float(input(f"Salário negativo! Dê o {i+1}º intervalo mínimo de salário: "))
    max = float(input(f"Dê o {i+1}º intervalo máximo de salário: "))
    if max < min:
        max = int(input(f"Errado! Dê o {i+1}º intervalo máximo de salário: "))
    else:
        qtd = 0
        print(f"Pessoas na faixa R$ {min:.2f} ~ R$ {max:.2f} de salário: ")
        for cpf in tab:
            if min <= tab[cpf][1] and max >= tab[cpf][1]:
                qtd += 1
                print(f"CPF {cpf}: {tab[cpf][0].title()}, R$ {tab[cpf][1]:.2f} de salário")
                soma += tab[cpf][1]
        print(f"Total de pessoas na faixa R$ {min:.2f} ~ R$ {max:.2f}: {qtd}")
        print(f"Média de salários na faixa R$ {min:.2f} ~ R$ {max:.2f}: R$ {soma/qtd:.2f}")
        if qtd == 0:
            print(f"Nenhuma pessoa encontrada na faixa R$ {min:.2f} ~ R${max:.2f} de salário")
            
            




# codigo_centro = int(input("Código do centro para pesquisar: "))
# while codigo_centro < 1:
#     codigo_centro = int(input("Inválido. Digite novamente o código do centro a ser pesquisado: "))

# while codigo_centro > 0:
#     qtd = 0
#     print(f"Cursos do centro {codigo_centro}: ")
#     for chave in tab:
#         if codigo_centro == tab[chave][1]:
#             qtd += 1
#             print(f"   {chave}: {tab[chave][0]}")
#     if qtd == 0:
#         print(f"Nenhum curso encontrado no centro {codigo_centro}")        
#     codigo_centro = int(input("Código do centro para pesquisar: "))
# print("Fim do programa.")
